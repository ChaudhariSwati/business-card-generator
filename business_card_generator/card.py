from datetime import date
from io import BytesIO
from typing import Any, Optional
from pydantic import BaseModel, EmailStr, HttpUrl, field_validator
from segno import QRCode, helpers, make_qr


class ContactCardParams(BaseModel):
    first_name: str
    last_name: str
    display_name: Optional[str] = None
    birth_date: Optional[date] = None
    organization: Optional[str] = None
    position: Optional[str] = None
    email_address: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    website_url: Optional[HttpUrl] = None
    profile_image: Optional[HttpUrl] = None
    address_street: Optional[str] = None
    address_city: Optional[str] = None
    address_zip: Optional[str] = None
    address_state: Optional[str] = None
    address_country: Optional[str] = None
    social_linkedin: Optional[HttpUrl] = None
    social_twitter: Optional[str] = None

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

    @field_validator("birth_date", "email_address", "website_url", "profile_image", "social_linkedin", mode="before")
    @classmethod
    def validate_empty_fields(cls, value: Optional[str]) -> Optional[str]:
        return value or None

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_display_name(self) -> str:
        return self.display_name or self.get_full_name()


class DigitalContactCard:
    params: ContactCardParams
    encoded_data: str
    qr_code: QRCode
    card_type: str = "contact"

    def __init__(self, params: ContactCardParams) -> None:
        self.params = params
        self.encoded_data = self._generate_encoded_data(params)
        self.qr_code = make_qr(self.encoded_data, encoding="utf-8", error="H")

    def _generate_encoded_data(self, params: ContactCardParams) -> str:
        raise NotImplementedError("Subclasses must implement _generate_encoded_data")

    def get_vcf_content(self) -> BytesIO:
        return BytesIO(self.encoded_data.encode("utf-8"))

    def get_svg_qr(self, scale_factor: float = 5.0) -> BytesIO:
        buffer = BytesIO()
        self.qr_code.save(buffer, kind="svg", scale=scale_factor, svgclass=self.card_type)
        buffer.seek(0)
        return buffer

    def get_png_qr(self, scale_factor: float = 5.0) -> BytesIO:
        buffer = BytesIO()
        self.qr_code.save(buffer, kind="png", scale=scale_factor)
        buffer.seek(0)
        return buffer

    def get_qr_data_url(self) -> str:
        """Return QR code as base64 data URL for embedding"""
        png_buffer = self.get_png_qr()
        import base64
        png_data = base64.b64encode(png_buffer.getvalue()).decode('utf-8')
        return f"data:image/png;base64,{png_data}"


class VCardFormat(DigitalContactCard):
    card_type: str = "vcard"

    def __init__(self, params: ContactCardParams) -> None:
        super().__init__(params)

    def _generate_encoded_data(self, params: ContactCardParams) -> str:
        # Build vCard data with enhanced fields
        vcard_data = helpers.make_vcard_data(
            name=f"{params.last_name};{params.first_name}",
            displayname=params.get_display_name(),
            nickname=params.display_name,
            birthday=params.birth_date,
            org=params.organization,
            title=params.position,
            email=params.email_address,
            phone=params.phone_number,
            url=str(params.website_url) if params.website_url else None,
            photo_uri=str(params.profile_image) if params.profile_image else None,
            street=params.address_street,
            city=params.address_city,
            region=params.address_state,
            zipcode=params.address_zip,
            country=params.address_country,
        )

        # Add custom social media fields if present
        if params.social_linkedin or params.social_twitter:
            lines = vcard_data.split('\n')
            insert_index = -2  # Before END:VCARD

            if params.social_linkedin:
                lines.insert(insert_index, f"X-SOCIALPROFILE;TYPE=linkedin:{params.social_linkedin}")

            if params.social_twitter:
                lines.insert(insert_index, f"X-SOCIALPROFILE;TYPE=twitter:{params.social_twitter}")

            vcard_data = '\n'.join(lines)

        return vcard_data


class MeCardFormat(DigitalContactCard):
    card_type: str = "mecard"

    def __init__(self, params: ContactCardParams) -> None:
        super().__init__(params)

    def _generate_encoded_data(self, params: ContactCardParams) -> str:
        # Build MeCard data with enhanced fields
        mecard_data = helpers.make_mecard_data(
            name=f"{params.last_name},{params.first_name}",
            nickname=params.display_name,
            birthday=params.birth_date.strftime("%Y%m%d") if params.birth_date else None,
            memo=params.organization,
            email=params.email_address,
            phone=params.phone_number,
            url=str(params.website_url) if params.website_url else None,
            houseno=params.address_street,
            city=params.address_city,
            zipcode=params.address_zip,
            prefecture=params.address_state,
            country=params.address_country,
        )

        # Add social media info as additional fields
        if params.social_linkedin:
            mecard_data += f";URL:{params.social_linkedin}"

        return mecard_data

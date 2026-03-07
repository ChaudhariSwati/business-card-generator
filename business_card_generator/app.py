import mimetypes

from http import HTTPStatus
from typing import Optional
from flask import Blueprint, Flask, abort, redirect, render_template, request, send_file
from pydantic import ValidationError
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.wrappers import Response
from whitenoise import WhiteNoise

from . import __about__
from .card import ContactCardParams, VCardFormat, MeCardFormat
from .settings import Settings


# ------------------------------------------------------------------------------


views_bp = Blueprint("views", __name__)


def contact_params_from_request() -> ContactCardParams:
    try:
        return ContactCardParams(**request.args.to_dict())
    except ValidationError:
        abort(HTTPStatus.UNPROCESSABLE_ENTITY)


@views_bp.get("/")
def get_home() -> str:
    return render_template("home.html")


@views_bp.get("/card")
def get_card() -> str:
    return render_template("card.html")


@views_bp.get("/vcard.svg")
def get_vcard_svg() -> Response:
    contact_params = contact_params_from_request()
    vcard = VCardFormat(contact_params)
    return send_file(
        vcard.get_svg_qr(),
        mimetype=mimetypes.types_map[".svg"],
        download_name="contact_vcard.svg",
    )


@views_bp.get("/vcard.png")
def get_vcard_png() -> Response:
    contact_params = contact_params_from_request()
    vcard = VCardFormat(contact_params)
    return send_file(
        vcard.get_png_qr(),
        mimetype=mimetypes.types_map[".png"],
        download_name="contact_vcard.png",
    )


@views_bp.get("/vcard.vcf")
def get_vcard_vcf() -> Response:
    contact_params = contact_params_from_request()
    vcard = VCardFormat(contact_params)
    return send_file(
        vcard.get_vcf_content(),
        mimetype=mimetypes.types_map[".vcf"],
        download_name="contact.vcf",
    )


@views_bp.get("/mecard.svg")
def get_mecard_svg() -> Response:
    contact_params = contact_params_from_request()
    mecard = MeCardFormat(contact_params)
    return send_file(
        mecard.get_svg_qr(),
        mimetype=mimetypes.types_map[".svg"],
        download_name="contact_mecard.svg",
    )


@views_bp.get("/mecard.png")
def get_mecard_png() -> Response:
    contact_params = contact_params_from_request()
    mecard = MeCardFormat(contact_params)
    return send_file(
        mecard.get_png_qr(),
        mimetype=mimetypes.types_map[".png"],
        download_name="contact_mecard.png",
    )


@views_bp.get("/mecard.vcf")
def get_mecard_vcf() -> Response:
    contact_params = contact_params_from_request()
    mecard = MeCardFormat(contact_params)
    return send_file(
        mecard.get_vcf_content(),
        mimetype=mimetypes.types_map[".vcf"],
        download_name="contact.vcf",
    )


# ------------------------------------------------------------------------------


def create_app(env_file: Optional[str] = ".env") -> Flask:
    # For serverless/production environments, skip .env file loading
    if env_file == ".env":
        try:
            settings = Settings(_env_file=env_file)
        except (FileNotFoundError, ValueError):
            # .env file not found, use defaults
            settings = Settings()
    else:
        # env_file is None, don't try to load from file
        settings = Settings()

    app = Flask(__name__)
    app.config.from_object(settings)
    app.config["about"] = dict(
        name=__about__.__name__,
        description=__about__.__description__,
        version=__about__.__version__,
    )
    app.debug = settings.app_environment == "development"
    app.testing = settings.app_environment == "testing"

    app.wsgi_app = WhiteNoise(  # type: ignore[method-assign]
        app.wsgi_app,
        root=app.static_folder,
        prefix=app.static_url_path,
        autorefresh=app.debug,
    )
    app.wsgi_app = ProxyFix(  # type: ignore[method-assign]
        app.wsgi_app, x_proto=1, x_host=1
    )

    @app.before_request
    def _force_https() -> Optional[Response]:
        if settings.force_https and request.url.startswith("http://"):
            https_url = request.url.replace("http://", "https://", 1)
            return redirect(https_url)
        return None

    app.register_blueprint(views_bp, url_prefix="")

    return app


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

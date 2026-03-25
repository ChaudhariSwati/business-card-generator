# 🔧 Business Card Generator – Personalized Version

This is a **customized version** of an open-source business card generator that creates QR-based digital cards in multiple formats like **vCard**, **MeCard**, **SVG**, and **PNG**.

I modified and deployed this project to:
- Learn about full-stack deployment
- Explore QR-based data encoding
- Customize UI, themes, and features

🌐 **[Live Demo](https://business-card-generator-plum.vercel.app/)** 🧑‍💻 **[My GitHub Fork](https://github.com/ChaudhariSwati/business-card-generator)**

---

## ✨ Features

- **New in v1.0.0**: Added international Country Code selection for phone numbers.
- Generate **vCard** / **MeCard** format QR codes.
- Export in **SVG**, **PNG**, or **VCF**.
- Live preview with a modern, professional UI.
- Powered by Flask + Python backend and React frontend.

---

## Usage

You can generate a business card directly using the [Live Demo](https://business-card-generator-plum.vercel.app/) or construct custom URLs for your profile:

*Example URL:**
```text
[https://business-card-generator-plum.vercel.app/vcard.svg?firstname=Swati&lastname=Chaudhari&job=Frontend+Developer&email=swatidchaudhary17@gmail.com&website=https://www.linkedin.com/in/swati-chaudhari-42b21a301](https://business-card-generator-plum.vercel.app/vcard.svg?firstname=Swati&lastname=Chaudhari&job=Frontend+Developer&email=swatidchaudhary17@gmail.com&website=https://www.linkedin.com/in/swati-chaudhari-42b21a301)
👉 Click here to view my Digital Business Card (SVG)🛠️ Tech StackFrontend: React.js, Tailwind CSSBackend: Python (Flask)Deployment: VercelExtras: GitHub Actions (CI/CD), QR generation libraries🧠 What I LearnedWorking with URL-based parameter passing.Handling image and card rendering via query strings.Deploying Flask + static frontend on platforms like Vercel.Understanding QR standards like vCard and MeCard.📦 Setup for DevelopmentBashcp .example.env .env
uv sync
uv run flask run
🙏 Original Author CreditThis project is originally created by Romain Clement.My version is a fork with UI and usage-level customizations for portfolio purposes.📜 LicenseThis project is distributed under the GNU AGPLv3 License.

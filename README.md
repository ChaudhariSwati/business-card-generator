# 🔧 Business Card Generator – Personalized Version

This is a **customized version** of an open-source business card generator that creates QR-based digital cards in multiple formats like **vCard**, **MeCard**, **SVG**, and **PNG**.

I modified and deployed this project to:
- Learn about full-stack deployment
- Explore QR-based data encoding
- Customize UI, themes, and features

🌐 **[Live Demo](https://business-card-generator-plum.vercel.app/)** 🧑‍💻 **[My GitHub Fork](https://github.com/ChaudhariSwati/business-card-generator)**

---

## ✨ Features

- Generate **vCard** / **MeCard** format QR codes
- Export in **SVG**, **PNG**, or **VCF**
- Live preview and customization options
- Responsive and deployable with one click
- Powered by Flask + Python backend and modern frontend stack

---

## Usage

You can generate a business card directly using the deployed version or construct custom URLs like this:

```text
[https://business-card-generator-plum.vercel.app/vcard.svg?firstname=Swati&lastname=Chaudhari&job=Frontend+Developer&email=swatidchaudhary17@gmail.com&website=https://www.linkedin.com/in/swati-chaudhari-42b21a301](https://business-card-generator-plum.vercel.app/vcard.svg?firstname=Swati&lastname=Chaudhari&job=Frontend+Developer&email=swatidchaudhary17@gmail.com&website=https://www.linkedin.com/in/swati-chaudhari-42b21a301)

Or as a clickable link:View My Digital Business Card (SVG)🛠️ Tech StackFrontend: React.js, Tailwind CSSBackend: Python (Flask)Deployment: VercelExtras: GitHub Actions (CI/CD), QR generation libraries🧠 What I LearnedWorking with URL-based parameter passingHandling image and card rendering via query stringsDeploying Flask + static frontend on platforms like VercelHow QR standards like vCard and MeCard work📦 Setup for DevelopmentBashcp .example.env .env
uv sync
uv run flask run
VSCode debugging:JSON{
  "FLASK_APP": "business_card_generator.app:create_app",
  "FLASK_ENV": "development"
}
🙏 Original Author CreditThis project is originally created by Romain Clement.My version is a fork with UI and usage-level customizations for portfolio purposes.Original repo: rclement/business-card-generator📜 LicenseThis project is distributed under the GNU AGPLv3 License.
---

### Key Changes Made:
* **Domain Swap**: Replaced the broken `business-card-generator.vercel.app` with your working `business-card-generator-plum.vercel.app`.
* **Live Demo Fix**: Updated the main demo link to point to the `plum` version.
* **Link Readability**: Simplified the clickable link text so it's not

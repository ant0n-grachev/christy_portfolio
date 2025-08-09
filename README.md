# 🎨 Christy Portfolio

> A lovingly crafted, customizable portfolio website built with Django — made for my girlfriend, so she can effortlessly share her art with the world. 💖

---

## 🌟 The Story

My girlfriend, an incredibly talented art student, needed a personal online space to showcase her growing collection of drawings and videos. But every platform we tried was either bloated, impersonal, or required too much tech setup on her part.

So I built a media-rich, fully customizable portfolio that empowers her (and now, potentially others) to manage and update her work with zero code involved.

This isn’t just a tech project. It’s a real, deployed site with a real user, created with love and the goal of being as artist-friendly as possible.

---

## 🌍 Live Demo

🔗 [https://portfolio.christypan.me](https://portfolio.christypan.me)

---

## 🖼️ Features

* **🎥 Media-rich entries**: Each post supports a title, description, image, and optionally a video with automatic validation to ensure a cover image is present if a video is uploaded.
* **📌 “Pinned” works**: Favorite creations can be spotlighted using a simple toggle.
* **🎨 Fully customizable theme**: Colors, header text, intro messages, button visibility, labels; all editable from the admin panel via a single `SiteSettings` record.
* **🖥️ Responsive UI**: Clean and minimalistic Bootstrap templates ensure it looks great on mobile and desktop.
* **🩹 Auto-cleanup logic**: Deleted media is removed via signals, and default settings are created automatically after migrations.
* **🌐 Deployed to Azure**: Media is served from Azure Blob Storage, and static files are optimized using WhiteNoise. Ready for real-world production use.
* **🚀 One-step deployment**: A `startup.sh` script installs dependencies, applies migrations, collects static files, and launches Gunicorn for robust server setups.

---

## 📸 Screenshots

### 🖼️ Home Page

A clean grid of artworks with media badges and pinned labels:
<img width="1582" height="955" alt="Screenshot 2025-08-06 at 11 55 34 AM" src="https://github.com/user-attachments/assets/b67e600c-2e20-406b-a603-85bf3b4731b3" />


### 🎥 Post Detail Page

Detailed view of an artwork post with description, title, and fully functional video player. The favicon displays at the top:
<img width="1582" height="955" alt="Screenshot 2025-08-06 at 11 58 13 AM" src="https://github.com/user-attachments/assets/0542802c-4a29-49b4-a23f-84912bde5ded" />


### 📄 Admin Dashboard

Django admin where new posts can be added, edited, or deleted. Easily manage artwork and site appearance:
<img width="1582" height="955" alt="Screenshot 2025-08-06 at 11 56 01 AM" src="https://github.com/user-attachments/assets/5ffc3c26-ed87-4851-a051-03b7175604af" />
<img width="1582" height="955" alt="Screenshot 2025-08-06 at 11 56 17 AM" src="https://github.com/user-attachments/assets/dae54262-78c2-4cbc-81a7-5bbcf0ae6351" />
<img width="1582" height="955" alt="Screenshot 2025-08-06 at 11 57 07 AM" src="https://github.com/user-attachments/assets/aa1e5457-df09-410a-9b18-c7b77a4167a3" />


---

## 🔧 Tech Stack

* **Backend**: Django 5
* **Frontend**: Bootstrap 5
* **Database**: Azure SQL (SQL Server)
* **Storage**: Azure Blob Storage (for uploaded media)
* **Static Files**: WhiteNoise
* **Deployment**: Gunicorn + Azure App Service

---

## 🛠️ Getting Started (Development)

```bash
# 1. Clone the repo
git clone https://github.com/your-username/christy-portfolio.git
cd christy-portfolio

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. (Optional) Create an admin user
python manage.py createsuperuser

# 5. Start the server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the portfolio, and `http://127.0.0.1:8000/admin/` to manage artworks and settings.

---

## 🚀 Production Deployment

1. Configure environment variables:

   * `SECRET_KEY`
   * `DEBUG` (False)
   * `ALLOWED_HOSTS`
   * `DATABASE_URL` (Azure SQL)
   * Azure storage credentials (`AZURE_ACCOUNT_NAME`, `AZURE_ACCOUNT_KEY`, `AZURE_CONTAINER`)
2. Run the `startup.sh` script:

   ```bash
   ./startup.sh
   ```

   This will:

   * Install Python dependencies
   * Apply database migrations
   * Collect static files
   * Start Gunicorn

---

## 🧬 Motivation

Christy Portfolio is about **giving control back to artists**. No ads, no paywalls, no templates that don't fit. Just a clean canvas tailored for showcasing creative work.

---

## 📬 Contributions Welcome!

Want to add more features, like categories or multilingual support? Feel free to fork and submit a PR!

---

## 📄 License - MIT

Do whatever you want, just don’t forget the original intent: helping creators shine 🌟

# Sociale

**Sociale** is a phishing awareness and simulation platform built with Django + REST APIs to help organizations train users, monitor susceptibility, and reinforce cybersecurity behavior.

## 🚀 Features

- Phishing awareness and simulation campaigns  
- Multi-factor authentication (MFA) with Google/Microsoft authenticator (QR) integration  
- Fine‑grained user roles & object‑level permissions  
- Dynamic phishing template generation  
- One‑pixel email tracking to detect opens  
- Dark web leak checking  
- Email open tracking simulation  
- Campaign and user analytics dashboards  

## 🏗️ Architecture & Tech Stack

- **Backend**: Django, Django REST Framework  
- **Database**: SQLite (default) — can be swapped for PostgreSQL, MySQL, etc.  
- **Authentication**: MFA via QR code (Google/Microsoft Authenticator)  
- **Permissions**: Role‑based and object level  
- **Email tracking**: One-pixel “open” tracking  
- **Leak detection**: Dark web data dump checks  
- **Templates**: Dynamic phishing site templates  
- **Front-end / APIs**: HTML / REST endpoints  
- **Deployment**: Dockerfile included for containerization  
- **CI**: Azure Pipelines (yaml config included)  

## 📂 Repository Structure

```
Sociale/
├── campaign/                  # Campaign-related logic & models  
├── exploit_data/              # Leak dump / dark web data  
├── group/                     # User groups, roles, permissions  
├── media/                     # Uploaded media, assets  
├── qrotp/                     # One-time / email tracking modules  
├── sociale/                   # Main Django project  
├── template/                  # Base templates  
├── templates/                 # HTML templates  
├── user/                      # User and profile models  
├── Dockerfile  
├── azure-pipelines.yml  
├── manage.py  
├── openapi-schema.yml         # API schema  
├── requirements.txt  
 
```

## 🛠️ Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/jonamadk/Sociale.git
   cd Sociale
   ```

2. **Create a virtual environment & install dependencies**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**  
   Copy or create `.env` (or similar) with settings such as `SECRET_KEY`, email server settings, etc.

4. **Apply migrations & seed data**  
   ```bash
   python manage.py migrate
   python manage.py loaddata initial_data.json  # if provided
   ```

5. **Run the development server**  
   ```bash
   python manage.py runserver
   ```

6. **Access the app**  
   Open your browser at `http://127.0.0.1:8000/`

7. **Docker**  
   To build & run via Docker:  
   ```bash
   docker build -t sociale .
   docker run -d -p 8000:8000 sociale
   ```

## 🔧 Usage Examples & Workflow

- Create and launch phishing campaigns  
- Track email opens via embedded one-pixel  
- Evaluate user click/response behavior  
- View analytics dashboards of campaign performance  
- Assign roles and permissions to administrators, campaign managers, and users  
- Use MFA to secure access  
- Monitor for leaked credentials using dark web dumps  

## ✅ Running Tests

If test suites exist, you can run:

```bash
python manage.py test
```

You may also consider adding CI checks for code coverage, linting, etc.

## 📈 Roadmap & Future Enhancements

- Support for more email service providers & SMTP integrations  
- Richer phishing template builder / UI editor  
- Advanced analytics (click heatmaps, cohort analysis)  
- Scheduled / recurring campaigns  
- Real-time dashboard updates  
- Multi-tenant support for organizations  
- Switching from SQLite to a production-grade DB (e.g. PostgreSQL)  

## 🧑‍💻 Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/xyz`)  
3. Make your changes + tests  
4. Submit a pull request  

Please follow the code style and include tests for new features.

## 📄 License

 MIT.

---

Thanks for using **Sociale** — may it help make organizations safer and more security-aware!

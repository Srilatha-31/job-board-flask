# Job Board

## 📌 Project Overview

Job Board is a responsive web application built using **Flask** that helps users browse job listings, search jobs, filter jobs based on location and job type, and view complete job details. The application provides a clean and user-friendly interface designed for a smooth job-search experience.

---

## 🚀 Live Demo

**Vercel Deployment:**
https://job-board-flask-8sbf.vercel.app

---

## 💻 GitHub Repository

https://github.com/Srilatha-31/job-board-flask

---

## ✨ Features

* Browse available job listings
* Search jobs by title or company
* Filter jobs by location
* Filter jobs by job type
* View detailed job information
* Apply Now button redirects users to the company's official careers page
* About page
* Contact page
* Responsive design using Bootstrap 5
* Smooth scrolling and hover animations
* Scroll-to-top button
* GitHub Actions CI pipeline
* Vercel deployment

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Data Storage

* JSON

### Deployment

* GitHub
* GitHub Actions
* Vercel

---

## 📂 Project Structure

```text
JobBoard/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── job_details.html
│   ├── about.html
│   └── contact.html
│
├── app.py
├── jobs.json
├── requirements.txt
├── vercel.json
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Srilatha-31/job-board-flask.git
```

### Navigate to the Project

```bash
cd job-board-flask
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🔄 CI/CD

This project uses **GitHub Actions** for Continuous Integration.

Whenever code is pushed to the **main** branch:

* Dependencies are installed automatically.
* The Flask application is validated.
* Syntax errors are detected before deployment.

The application is automatically deployed using **Vercel** after successful updates.

---
## 🔮 Future Enhancements

* User authentication
* Admin dashboard
* Save jobs
* Job application tracking
* Database integration using MySQL
* Email notifications
* Pagination
* Company logos
* Dark mode

---

## 👩‍💻 Author

**Darsi Sri Latha**

B.Tech – Information Technology

---

## 📄 License

This project was developed for educational and assessment purposes.

# 🔗 URL Shortener Web Application

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

A clean and lightweight **URL Shortener** built using Flask and SQLite.\
This application allows users to convert long URLs into short, shareable
links with optional custom aliases and built-in click tracking.

------------------------------------------------------------------------

## 🚀 Features

-   🔗 Shorten long URLs
-   ✨ Custom alias support
-   🔄 Automatic unique short code generation
-   📊 Click tracking (analytics)
-   🔍 Search functionality
-   🗑 Delete saved URLs
-   🕒 Created timestamp tracking
-   🎨 Clean Bootstrap-based UI

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python
-   Flask
-   SQLite
-   SQLAlchemy
-   Bootstrap 5

------------------------------------------------------------------------

## ⚙️ How It Works

1.  User enters a long URL.
2.  The system generates a unique short code (or accepts a custom
    alias).
3.  The short link is stored in the database.
4.  When accessed:
    -   The application redirects to the original URL.
    -   The click counter increases automatically.


------------------------------------------------------------------------

## ▶️ Installation & Setup

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/mitalic0/URL-Shortener.git
cd URL-Shortener
```

### 2️⃣ Create a Virtual Environment

``` bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

``` bash
python app.py
```

Open in browser:

http://127.0.0.1:5000


------------------------------------------------------------------------

## 🔮 Future Improvements

-   User authentication system
-   QR code generation
-   Link expiration feature
-   Analytics dashboard with charts
-   REST API endpoint support

------------------------------------------------------------------------

## 📄 License

This project is developed for educational purposes.

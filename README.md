# 📸 Django Social Media App

A full-featured **social media web application** built with **Django**, allowing users to register, share image-based posts, like and comment on others' posts, and manage their profiles.

---

## 🚀 Features

- 👤 **User Authentication** – Sign up, login, logout
- 🖼️ **Post Creation** – Upload posts with images, titles, and captions
- 📰 **Feed** – View all posts in a chronological feed
- ❤️ **Likes** – Like/unlike posts with real-time feedback using AJAX
- 💬 **Comments** – Add and view comments on posts
- 🧑 **User Profile** – Profile photo upload and profile editing
- 🔒 **Password Management** – Password change and reset via email

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, AJAX
- **Database**: SQLite3
- **Authentication**: Django’s built-in auth system
- **Media Handling**: Django static/media file serving

---

## 📂 Project Structure Overview

```

socialproject/
│
├── users/         # Authentication and profile management
├── posts/         # Post, like, comment functionality
├── templates/     # HTML templates
├── media/         # Uploaded images
├── static/        # Static CSS/JS files
├── db.sqlite3     # SQLite database
├── manage.py      # Django entry point
└── requirements.txt

````

---

## ⚙️ Setup & Installation

> 🔧 Prerequisites: Python 3.8+, pip, and virtualenv (recommended)

```bash
# 1. Clone the repository
git clone https://github.com/imsaqib04/social-media-app.git
cd social-media-app

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
````

Visit: `http://127.0.0.1:8000/`

---

## 🔐 Auth & User Management URLs

| URL                       | Description              |
| ------------------------- | ------------------------ |
| `/users/register/`        | User registration        |
| `/users/login/`           | User login               |
| `/users/logout/`          | Logout (GET/POST)        |
| `/users/edit/`            | Edit profile             |
| `/users/password_change/` | Change password          |
| `/users/password_reset/`  | Reset password via email |

---

## 📝 Post & Feed URLs

| URL               | Description               |
| ----------------- | ------------------------- |
| `/posts/create/`  | Create a new post         |
| `/posts/feed/`    | View the feed             |
| `/posts/like/`    | Like/unlike a post (AJAX) |
| `/posts/comment/` | Add a comment             |

---

## 📸 Screenshots

---

<img width="1919" height="953" alt="image" src="https://github.com/user-attachments/assets/44b44905-e0c9-4892-bebe-337110ec585f" />

<img width="1911" height="942" alt="image" src="https://github.com/user-attachments/assets/7a5ae9ed-386a-45a6-a27f-8d4c259b1f5c" />

<img width="1916" height="953" alt="image" src="https://github.com/user-attachments/assets/612ae812-0ad0-4b50-8601-826a77dacd0f" />


---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Mohd Saqib**
GitHub: [@imsaqib04](https://github.com/imsaqib04)

---

## ⭐ Star the Repo

If you find this project useful, please give it a ⭐ on GitHub — it helps a lot!

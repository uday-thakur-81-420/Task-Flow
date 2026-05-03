# TaskFlow 🌿
### A Full-Stack Team Task Management System
#ADMIN Username : Shubham , Pass : @@@@Ut4202507
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Railway-336791?style=flat&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap&logoColor=white)
![Railway](https://img.shields.io/badge/Deployed-Railway-0B0D0E?style=flat&logo=railway&logoColor=white)

---

## 🌐 Live Demo

**[task-flow-production-dc98.up.railway.app](https://task-flow-production-dc98.up.railway.app)**

---

## 📌 About The Project

TaskFlow is a full-stack web application that allows teams to manage projects, assign tasks, and track progress — with a clean role-based access control system for Admins and Members.

Built with pure Django (no REST Framework) using server-side rendering with Django Templates.

---

## ✨ Features

### 🔐 Authentication
- User Signup & Login
- Session-based authentication
- Automatic logout

### 👥 Role-Based Access Control
| Feature | Admin | Member |
|---|---|---|
| Create Projects | ✅ | ❌ |
| Create Tasks | ✅ | ❌ |
| Assign Tasks | ✅ | ❌ |
| Edit / Delete Tasks | ✅ | ❌ |
| View All Tasks | ✅ | ❌ |
| View Assigned Tasks | ✅ | ✅ |
| Update Task Progress | ✅ | ✅ |
| Add Comments | ✅ | ✅ |

### 📁 Project Management
- Create and manage multiple projects
- Add team members to projects
- View project-wise task count

### ✅ Task Management
- Create tasks with title, description, priority, due date
- Assign tasks to specific team members
- Kanban-style board — To Do / In Progress / Done
- One-click status updates from dashboard

### 📊 Progress Tracking
- Circular progress chart (0–100%) per task
- Interactive slider for manual progress updates
- Auto status change based on progress (0% → To Do, 1-99% → In Progress, 100% → Done)
- Overall progress bar on dashboard
- Donut chart showing task breakdown by status

### 💬 Comments System
- Add comments on any task
- View all comments with author name and timestamp
- Keeps communication organized within tasks

### ⚠️ Overdue Detection
- Automatically detects overdue tasks
- Red alert banner on dashboard
- Overdue badge on task cards

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 (Pure — no DRF) |
| Frontend | Django Templates + Bootstrap 5 |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Auth | Django Built-in Auth |
| Static Files | Whitenoise |
| Deployment | Railway |
| Version Control | GitHub |

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.12+
- pip
- Git

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/uday-thakur-81-420/Task-Flow.git
cd Task-Flow

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser (Admin)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```

Visit: `http://127.0.0.1:8000`

---

## 📁 Project Structure

```
taskflow_project/
├── taskflow/               ← Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/               ← Auth, Signup, Login, Profiles
│   ├── models.py           ← Profile model with roles
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── projects/               ← Project & Team management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── tasks/                  ← Task CRUD, Comments, Progress
│   ├── models.py           ← Task + Comment models
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── dashboard/              ← Dashboard with charts
│   ├── views.py
│   └── urls.py
├── templates/              ← All HTML templates
│   ├── base.html
│   ├── accounts/
│   ├── dashboard/
│   ├── tasks/
│   └── projects/
├── static/
│   └── css/
│       └── style.css       ← Custom green theme
├── requirements.txt
├── Procfile
└── manage.py
```

---

## 🗃️ Database Models

### Profile
```
User (OneToOne) | role (admin/member)
```

### Project
```
name | description | created_by | members (M2M) | created_at
```

### Task
```
title | description | project (FK) | assigned_to (FK)
status | priority | due_date | progress | created_at
```

### Comment
```
task (FK) | author (FK) | text | created_at
```

---

## 🌍 Deployment (Railway)

```bash
# Required files
Procfile     → web: gunicorn taskflow.wsgi --bind 0.0.0.0:$PORT --log-file -
requirements.txt

# Environment Variables on Railway
SECRET_KEY              = your-secret-key
DEBUG                   = False
DATABASE_URL            = (auto-set by Railway PostgreSQL)
CSRF_TRUSTED_ORIGINS    = https://your-domain.up.railway.app
```

---

## 🎨 Color Theme

| Color | Hex | Usage |
|---|---|---|
| Dark Green | `#1a3a2e` | Sidebar, Headings |
| Mid Green | `#2d6a4f` | Buttons, Active states |
| Accent | `#52b788` | Progress bars, Badges |
| Light Green | `#b7e4c7` | Sidebar text |
| Gold | `#d4a017` | In Progress, Badges |
| Background | `#f0f7f2` | Page background |

---

## 📸 Screenshots

> Dashboard — Kanban Board with Progress Charts

> Task Detail — Progress Slider + Comments

> Login Page — Clean Auth UI

---

## 👨‍💻 Author

**Uday Thakur**
- GitHub: [@uday-thakur-81-420](https://github.com/uday-thakur-81-420)
- Live: [task-flow-production-dc98.up.railway.app](https://task-flow-production-dc98.up.railway.app)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ using Django
</div>

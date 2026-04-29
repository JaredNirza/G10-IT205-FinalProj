# SupplySync Office Manager

## A web-based office management system built with Django for managing inventory items, employees, and supply requests

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [User Roles](#user-roles)
- [Application Modules](#application-modules)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Support](#support)
- [Version History](#version-history)
- [License](#license)

---

## Overview

SupplySync Office Manager is a Django web application for tracking office inventory, managing employees, and handling internal supply requests. It includes basic authentication, a simple dashboard, and CRUD modules to support day-to-day office operations.

---

## Features

- Authentication (register, login, logout)
- Dashboard summary (inventory count, employee count, pending requests)
- Inventory management (create, view, update, delete) with search
- Employee management (create, view, update, delete) with search
- Supply request management (create, view, update, delete) with status filtering (Pending/Approved/Fulfilled)

---

## System Requirements

| Requirement | Version                        |
| ----------- | ------------------------------ |
| Python      | 3.10 or higher                 |
| Django      | 5.2 or higher                  |
| Database    | SQLite (default) or PostgreSQL |
| Browser     | Chrome, Firefox, Edge, Safari  |

**Recommended:**

- 4GB RAM minimum
- 1GB free disk space
- Internet connection (for Bootstrap CDN)

---

## Installation

**Using [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) package manager**

1. **Clone or download the project**

   ```bash
   git clone https://github.com/JaredNirza/G10-IT205-FinalProj.git
   cd G10-IT205-FinalProj
   ```

2. **Install dependencies**

   > Install uv (skip if already installed)

   ```bash
   pip install uv
   # or
   pipx install uv
   ```

   ```bash
   uv sync
   ```

3. **Run Project**

   ```bash
   uv manage.py runserver
   ```

4. **Run Migrations**

   ```bash
   uv manage.py migrate
   ```

5. **Create a superuser account**

   ```bash
   uv manage.py createsuperuser
   ```

---

**Install manually**

1. **Clone or download the project**

   ```bash
   git clone https://github.com/JaredNirza/G10-IT205-FinalProj.git
   cd G10-IT205-FinalProj
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   ```bash
   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt

   # Or if using uv
   uv pip install -r requirements.txt
   ```

5. **Run project**

   ```bash
   python manage.py runserver
   ```

6. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser account**

   ```bash
   python manage.py createsuperuser
   ```

---

## Running the Application

### Development Server

1. Activate your virtual environment
2. Run the development server:

   ```bash
   uv manage.py runserver
   # or
   python manage.py runserver
   ```

3. Open your browser and navigate to: `http://127.0.0.1:8000/`

### Admin Panel

Access the admin panel at: `http://127.0.0.1:8000/admin/`

---

## User Roles

| Role               | What They Can Do                                              |
| ------------------ | ------------------------------------------------------------- |
| **Guest**          | View landing page, login, register                            |
| **Staff/Employee** | Use Inventory, Staff, and Requests modules after logging in   |
| **Admin**          | Full access via Django admin (`/admin/`) plus all app modules |

Note: On signup, the app creates an `Employee` profile linked to the new Django `User`.

---

## Application Modules

- `office_manager/`: Django project config (settings/urls/views) and home dashboard
- `inventory/`: Office items inventory (CRUD + search)
- `staff/`: Employee directory (CRUD + search)
- `requests/`: Supply requests (CRUD + status filtering)
- `templates/`: Shared templates (Bootstrap-based UI)

---

## Project Structure

```
G10-IT205-FinalProj/
├── manage.py
├── office_manager/          # Django project settings/urls/views
├── inventory/               # Inventory app
├── staff/                   # Staff app
├── requests/                # Requests app
├── templates/               # Global templates (base, landing, home, auth)
├── db.sqlite3               # Local SQLite database (dev)
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Configuration

Key settings live in `office_manager/settings.py`.

| Setting         | Description                                     |
| --------------- | ----------------------------------------------- |
| `DEBUG`         | Keep `True` for dev, set `False` for production |
| `ALLOWED_HOSTS` | Add your hostnames/IPs when deploying           |
| `DATABASES`     | Uses SQLite by default (`db.sqlite3`)           |

Admin access:

1. Create a superuser (`uv manage.py createsuperuser`)
2. Visit `http://127.0.0.1:8000/admin/`

---

## Support

Open an issue in the repository describing:

1. Steps to reproduce
2. Expected vs actual behavior
3. Screenshots (if UI-related)
4. Your Python and Django versions

---

## Version History

**Version 1.0** - Initial Release

- Inventory management
- Employee management
- Supply requests
- Dashboard summary
- Authentication (signup/login/logout)

---

## License

`MIT License`

---

_© 2026 SupplySync Office Manager_

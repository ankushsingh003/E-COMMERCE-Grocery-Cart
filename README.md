# 🛒 E-Commerce Grocery Cart

A full-stack grocery store web application built with **Flask** (Python) and **MySQL**, featuring a dynamic frontend, real-time search, cart management, and user authentication.

## ✨ Features

- **Product Catalog**: Dynamic product listing with images, prices, and unit of measure.
- **Search & Filter**: Real-time product filtering as you type.
- **Shopping Cart**: Add items, update quantities, calculate totals, and checkout.
- **User Authentication**: Login/Logout system with session management.
- **Admin Dashboard**: Manage products (Add/Edit) and view orders.
- **Responsive Design**: Modern UI with CSS animations and hover effects.
- **Cloud-Ready**: Configured for deployment on platforms like Render.

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL (Local) / Aiven/TiDB (Cloud)
- **Frontend**: HTML5, CSS3, JavaScript (jQuery, Bootstrap)
- **Deployment**: Render / Gunicorn

## 🚀 Setup Instructions

### Prerequisites
- Python 3.x
- MySQL Server

### 1. Clone the Repository
```bash
git clone https://github.com/ankushsingh003/E-COMMERCE-Grocery-Cart.git
cd E-COMMERCE-Grocery-Cart
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Setup

#### Option A: Local Setup
1.  Make sure your local MySQL server is running.
2.  Import the database schema (if you have the dump) or run the `backend/export_db.py` script to generate `init_cloud_db.sql` and run that in your SQL workbench.
3.  The app defaults to `localhost`, `root`, `sangita143@H`, `gs`.

#### Option B: Cloud/Remote Setup
1.  Create a MySQL database on a cloud provider (Aiven, TiDB, etc.).
2.  Run the SQL from `backend/init_cloud_db.sql` in your cloud database console.
3.  Set Environment Variables (see below).

### 4. Running the Application
```bash
cd backend
python server.py
```
The app will run at `http://127.0.0.1:5000`.

## ⚙️ Configuration (Environment Variables)

The application supports the following environment variables for configuration. These are **required** for cloud deployment but optional for local development (defaults are provided).

| Variable | Description | Default (Local) |
| :--- | :--- | :--- |
| `DB_HOST` | Database Hostname | `localhost` |
| `DB_USER` | Database Username | `root` |
| `DB_PASSWORD` | Database Password | `sangita143@H` |
| `DB_NAME` | Database Name | `gs` |
| `SECRET_KEY` | Flask Session Secret | `super_secret_key` |

## ☁️ Deployment (Render)

1.  **New Web Service**: Connect your GitHub repo to Render.
2.  **Runtime**: Python 3.
3.  **Build Command**: `pip install -r requirements.txt`
4.  **Start Command**: `gunicorn --chdir backend server:app`
5.  **Environment Variables**: Add the `DB_*` and `SECRET_KEY` variables in the dashboard.

## 📂 Project Structure

```
E-COMMERCE-Grocery-Cart/
├── UI/
│   ├── static/          # CSS, JS, Images
│   └── templates/       # HTML Files
├── backend/
│   ├── server.py        # Flask App Entry Point
│   ├── product_sql.py   # Database Logic
│   └── init_cloud_db.sql # DB Migration Script
├── requirements.txt
└── README.md
```

## 📝 API Endpoints

- `GET /products`: Fetch all products.
- `POST /insertOrder`: Create a new order.
- `POST /products`: Add a new product (Admin).
- `POST /login`: User authentication.

---
*Built with ❤️ by Ankush Kumar Singh*

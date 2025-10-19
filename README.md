# 🧩 Capstone Project - Design Phase

## 1. Introduction

This document continues from **Part 1: The Idea and Planning Phase** of the Capstone Project.
In Part 1, I defined the project concept, features, database plan, and development timeline.
In this **Design Phase**, I present:

* The **Entity Relationship Diagram (ERD)**, showing how data will be structured and related.
* A detailed list of the **API endpoints** that will form the backbone of the application.

These will serve as the blueprint for the implementation phase (Part 3).

---

## 2. Entity Relationship Diagram (ERD)

### 2.1 Overview

The E-commerce Product API consists of three core entities:

1. **User** — represents store administrators and registered users (leveraging Django’s built-in `User` model).
2. **Category** — represents product categories such as “Electronics,” “Clothing,” or “Books.”
3. **Product** — represents individual products listed in the store.

The **relationships** are:

* Each **Product** belongs to **one Category** (One-to-Many).
* Each **Category** can have **multiple Products**.
* Each **Product** is **created by a User** (admin), establishing a link between users and products.

---

### 2.2 ERD Diagram

*(You will upload your ERD image here once you draw it using draw.io, Miro, or dbdiagram.io.)*

Here’s how the structure should look conceptually:

```
+-----------------+          1        +------------------+
|     Category    |------------------<|     Product      |
+-----------------+                   +------------------+
| id (PK)         |                   | id (PK)          |
| name            |                   | name             |
| created_at      |                   | description      |
| updated_at      |                   | price            |
+-----------------+                   | in_stock (bool)  |
                                      | category_id (FK) |
                                      | created_by (FK)  |
                                      | created_at       |
                                      | updated_at       |
                                      +------------------+
                                                ^
                                                |
                                                | Many
                                                |
                                          +-------------+
                                          |    User     |
                                          +-------------+
                                          | id (PK)     |
                                          | username     |
                                          | email        |
                                          | password     |
                                          | is_staff     |
                                          +-------------+
```

---

### 2.3 Description of Entities

#### **User (from Django’s default model)**

| Field    | Type                | Description                                             |
| -------- | ------------------- | ------------------------------------------------------- |
| id       | Integer (AutoField) | Primary key                                             |
| username | CharField           | Unique username for authentication                      |
| email    | EmailField          | User’s email address                                    |
| password | CharField           | Hashed password                                         |
| is_staff | Boolean             | Determines admin access for product/category management |

---

#### **Category**

| Field      | Type                | Description                                  |
| ---------- | ------------------- | -------------------------------------------- |
| id         | Integer (AutoField) | Primary key                                  |
| name       | CharField           | The category name (unique)                   |
| created_at | DateTimeField       | Timestamp when the category was created      |
| updated_at | DateTimeField       | Timestamp when the category was last updated |

**Relationships:**

* One-to-Many with Product (one Category → many Products)

---

#### **Product**

| Field       | Type                  | Description                        |
| ----------- | --------------------- | ---------------------------------- |
| id          | Integer (AutoField)   | Primary key                        |
| name        | CharField             | Product name                       |
| description | TextField             | Detailed product description       |
| price       | DecimalField          | Product price                      |
| in_stock    | BooleanField          | Availability status                |
| category    | ForeignKey (Category) | Category the product belongs to    |
| created_by  | ForeignKey (User)     | Admin user who created the product |
| created_at  | DateTimeField         | When the product was created       |
| updated_at  | DateTimeField         | When the product was last updated  |

---

## 3. API Endpoints Design

### 3.1 Overview

The API will follow **RESTful principles**, using **Django REST Framework (DRF)**.
Endpoints are grouped by functionality — **User Management**, **Category Management**, and **Product Management**.

All endpoints will return **JSON responses**.

---

### 3.2 Authentication

* **Authentication Type:** Token Authentication
* **Permissions:**

  * Authenticated admin users can create, update, and delete.
  * Anonymous users can only view products and categories.


---------------------------------------------------------------------------------------------

---
# FINAL SUMMARY

````markdown
# 🛒 E-commerce API (Django REST Framework)

This is a simple E-commerce API built with **Django** and **Django REST Framework** as part of the Capstone project.  
It provides basic functionality for **user authentication** and **product management**.

---

## 🚀 Features

### 👤 User Authentication
- **Register new users**
- **Login** with JWT tokens
- **Logout** (blacklist or discard tokens)
- **View / Update Profile**

### 🛍️ Product Management
- **Create / List / Update / Delete** products
- **Categorize** products by category
- **Public product listing** (accessible to everyone)
- **Private product management** (requires authentication)

---

## 🏗️ Technologies Used

- Python 3.12
- Django 5.x
- Django REST Framework
- Simple JWT (for authentication)
- PostgreSQL (can be replaced with SQLite)

---

## ⚙️ Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/django-ecommerce-project.git
   cd django-ecommerce-project
````

2. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```bash
   SECRET_KEY=your_secret_key_here
   DB_NAME=ecommerce-be
   DB_USER=ecommerce_user
   DB_PASSWORD=changeme
   DB_HOST=localhost
   DB_PORT=5432
   ```

   *(You can also switch to SQLite by uncommenting the default DB settings in `settings.py`.)*

5. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the admin panel**

   ```
   http://127.0.0.1:8000/admin/
   ```

---

## 🔑 API Endpoints

### 👤 User Endpoints

| Method    | Endpoint               | Description                |
| --------- | ---------------------- | -------------------------- |
| POST      | `/api/users/register/` | Register a new user        |
| POST      | `/api/users/login/`    | Login and get JWT tokens   |
| POST      | `/api/users/logout/`   | Logout and blacklist token |
| GET       | `/api/users/profile/`  | View user profile          |
| PUT/PATCH | `/api/users/profile/`  | Update user profile        |

---

### 🛍️ Product Endpoints

| Method    | Endpoint              | Description                          |
| --------- | --------------------- | ------------------------------------ |
| GET       | `/api/products/`      | List all products                    |
| POST      | `/api/products/`      | Create a new product (authenticated) |
| GET       | `/api/products/{id}/` | Retrieve a single product            |
| PUT/PATCH | `/api/products/{id}/` | Update a product                     |
| DELETE    | `/api/products/{id}/` | Delete a product                     |

---

## 🔐 Authentication

The project uses **JWT (JSON Web Tokens)** for secure user authentication.

After login:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

Use the access token in the `Authorization` header for protected endpoints:

```
Authorization: Bearer <access_token>
```

---

## 🧪 Testing the API with Postman

A ready-to-use Postman collection is included:
➡️ `Ecommerce-API.postman_collection.json`

Import it into Postman to test:

* User registration/login/logout
* Profile view/update
* CRUD for products

---

## 🧰 Folder Structure

```
ecommerceProject/
│
├── ecommerceProject/        # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── user/                    # User app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── products/                # Product app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── .env                     # Environment variables
├── requirements.txt
├── manage.py
└── Ecommerce-API.postman_collection.json
```

---

## 👨‍💻 Author

**Sherif Mohamed**
Capstone Project – ALX Backend Django
2025

```

---

## ✅ ③ Postman Collection Endpoints

Here’s a summary of what’s inside your Postman collection (`Ecommerce-API.postman_collection.json`):

### **Folders:**
1. **Auth**
   - `POST /api/users/register/`
   - `POST /api/users/login/`
   - `POST /api/users/logout/`
   - `GET /api/users/profile/`
   - `PUT /api/users/profile/`

2. **Products**
   - `GET /api/products/`
   - `POST /api/products/`
   - `GET /api/products/:id/`
   - `PUT /api/products/:id/`
   - `DELETE /api/products/:id/`

All requests use `{{base_url}}` (e.g., `http://127.0.0.1:8000`) and JWT `Bearer` authorization for protected routes.

---

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

---

### 3.3 API Endpoints Summary

#### **User Management**

| URL                    | Method | Action | Description                 | Auth Required |
| ---------------------- | ------ | ------ | --------------------------- | ------------- |
| `/api/users/register/` | POST   | Create | Register a new user         | ❌             |
| `/api/users/login/`    | POST   | Create | Obtain authentication token | ❌             |
| `/api/users/logout/`   | POST   | Action | Invalidate token / logout   | ✅             |

---

#### **Category Management**

| URL                         | Method      | Action   | Description                  | Auth Required  |
| --------------------------- | ----------- | -------- | ---------------------------- | -------------- |
| `/api/categories/`          | GET         | List     | Retrieve all categories      | ❌              |
| `/api/categories/`          | POST        | Create   | Add a new category           | ✅ (Admin only) |
| `/api/categories/<int:id>/` | GET         | Retrieve | Get details for one category | ❌              |
| `/api/categories/<int:id>/` | PUT / PATCH | Update   | Edit category details        | ✅ (Admin only) |
| `/api/categories/<int:id>/` | DELETE      | Delete   | Remove category              | ✅ (Admin only) |

---

#### **Product Management**

| URL                                   | Method      | Action   | Description                 | Auth Required  |
| ------------------------------------- | ----------- | -------- | --------------------------- | -------------- |
| `/api/products/`                      | GET         | List     | Retrieve all products       | ❌              |
| `/api/products/`                      | POST        | Create   | Add a new product           | ✅ (Admin only) |
| `/api/products/<int:id>/`             | GET         | Retrieve | Get product details         | ❌              |
| `/api/products/<int:id>/`             | PUT / PATCH | Update   | Update a product            | ✅ (Admin only) |
| `/api/products/<int:id>/`             | DELETE      | Delete   | Remove a product            | ✅ (Admin only) |
| `/api/products/search/?q=<name>`      | GET         | Search   | Search for products by name | ❌              |
| `/api/products/filter/?category=<id>` | GET         | Filter   | Filter products by category | ❌              |

---

### 3.4 Example API Response (for Reference)

**GET `/api/products/`**

```json
[
  {
    "id": 1,
    "name": "Wireless Mouse",
    "description": "A high-quality ergonomic mouse",
    "price": 29.99,
    "in_stock": true,
    "category": "Electronics",
    "created_by": "admin"
  }
]
```

---

## 4. Design Considerations

1. **Modular Structure**:

   * `users` app → manages registration, login, and authentication.
   * `products` app → manages products and categories.
2. **Security**:

   * Token authentication for all modifying operations.
3. **Scalability**:

   * Clear separation of concerns allows for adding more features later (e.g., orders, carts).
4. **Reusability**:

   * DRF `ModelViewSet` and routers simplify CRUD operations.









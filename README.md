Capstone Project - Part 1: The Idea and Planning Phase.

1. Project Idea and Main Features
E-commerce Product API. The core purpose of this API is to manage an online store's products, categories, and inventory.
The main features I'll build are:
Product Management: Users can add, view, update, and delete products. This will involve CRUD operations for products.
Category Management: Users can add, view, update, and delete product categories. This will also require CRUD operations.
Product Search and Filtering: Users can search for products by name or filter them by category. This is a crucial feature that goes beyond basic CRUD and demonstrates more complex query-building.
User Authentication: Users (e.g., store administrators) must be logged in to create, update, or delete products and categories. Public users can view products without logging in.

2. Django Apps and Endpoints
To keep the project organized, I’ll break it into at least two modular Django apps. This follows best practices for separation of concerns.
users app: This app will handle all user-related logic, including user registration and authentication.
products app: This app will manage all product and category-related logic.
Here is a breakdown of the core API endpoints for the products app:
URL
HTTP Method
Action
Description
/api/products/
GET
list
Get a list of all products (publicly accessible).
/api/products/
POST
create
Add a new product (admin only).
/api/products/<int:pk>/
GET
retrieve
Get details for a single product (publicly accessible).
/api/products/<int:pk>/
PUT / PATCH
update
Update a product's details (admin only).
/api/products/<int:pk>/
DELETE
destroy
Delete a product (admin only).
/api/categories/
GET
list
Get a list of all categories.
/api/categories/
POST
create
Add a new category (admin only).
/api/categories/<int:pk>/
DELETE
destroy
Delete a category (admin only).
/api/products/search/
GET
search
Search for products by name or filter by category.


3. Database Schema Design
A well-designed database is the backbone of your project. For this API, I will need at least three models.
User Model: I can use Django's built-in User model for authentication. No need to create a new one.
Category Model: This model will define product categories. A simple schema would include a name field.
name: A CharField to store the category's name.
Product Model: This is the central model of the API. It will have a relationship with the Category model.
name: A CharField for the product's name.
description: A TextField for product details.
price: A DecimalField for the product's price.
category: A ForeignKey to the Category model, linking each product to its category.
in_stock: A BooleanField to indicate if the product is available.



4. Design Considerations
Modular Structure:


users app → manages registration, login, and authentication.


products app → manages products and categories.


Security:


Token authentication for all modifying operations.


Scalability:


Clear separation of concerns allows for adding more features later (e.g., orders, carts).


Reusability:


DRF ModelViewSet and routers simplify CRUD operations.


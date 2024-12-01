## E-Commerce Backend Application with Django Rest Framework (DRF)

This project is a backend API for an e-commerce platform built using Django and Django Rest Framework. It provides APIs for user authentication, product management, and order management. Below are the details of the setup, testing, and usage instructions.

---

### **Features**
1. **User Management**: 
   - Registration and login.
   - JWT-based authentication.
2. **Product Management**: 
   - CRUD operations for products.
   - Only admins can delete products.
3. **Order Management**:
   - Place orders.
   - View order details (only for the user who placed the order).
4. **Permissions**:
   - Only authenticated users can access the API.
   - Admin permissions required for certain actions (e.g., deleting products).

---

### **Requirements**

- Python 3.10+
- Django 4.x
- Django Rest Framework (DRF)
- Django SimpleJWT for authentication
- SQLite (default database) or any other database supported by Django

---

### **Setup Instructions**

#### 1. **Clone the Repository**
```bash
git clone https://github.com/your-repo/ecommerce-backend.git
cd ecommerce-backend
```

#### 2. **Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
```

#### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

#### 4. **Run Migrations**
```bash
python manage.py migrate
```

#### 5. **Create a Superuser (Admin User)**
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

#### 6. **Start the Server**
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

---

### **API Endpoints**

#### **1. User Authentication**
- **Register a User**:  
  `POST /api/users/register/`  
  Request Body:
  ```json
  {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "testpassword"
  }
  ```
  Response: 
  ```json
  {
    "message": "User registered successfully"
  }
  ```

- **Login**:  
  `POST /api/users/login/`  
  Request Body:
  ```json
  {
    "username": "testuser",
    "password": "testpassword"
  }
  ```
  Response:
  ```json
  {
    "access": "your_jwt_access_token"
  }
  ```

#### **2. Product Management**
- **List Products**:  
  `GET /api/products/`  
  Headers:  
  ```json
  {
    "Authorization": "Bearer your_jwt_access_token"
  }
  ```

- **Create a Product (Admin Only)**:  
  `POST /api/products/`  
  Request Body:
  ```json
  {
    "name": "Sample Product",
    "description": "This is a sample product",
    "price": 99.99,
    "stock": 10
  }
  ```

- **Delete a Product (Admin Only)**:  
  `DELETE /api/products/<product_id>/`  

#### **3. Order Management**
- **List Orders**:  
  `GET /api/orders/`  

- **Create an Order**:  
  `POST /api/orders/`  
  Request Body:
  ```json
  {
    "total_amount": 199.99,
    "items": [
      {
        "product": 1,
        "quantity": 2,
        "price": 99.99
      }
    ]
  }
  ```

---

### **Testing the Application**

#### Using `curl`
Refer to the [previous `curl` commands](#).

#### Using Postman
1. Import the API collection (optional).
2. Set up the following endpoints:
   - `POST /api/users/register/`
   - `POST /api/users/login/`
   - `GET /api/products/`
   - `POST /api/products/`
   - `DELETE /api/products/<id>/`
   - `POST /api/orders/`
3. Add an `Authorization` header for endpoints requiring authentication:
   ```text
   Bearer your_jwt_access_token
   ```

---

### **Customizations**

- **Database**: Update the `DATABASES` configuration in `settings.py` to use a different database.
- **Environment Variables**: Use a `.env` file to manage sensitive data (e.g., secret key, database credentials).

---

### **Common Issues**

- **JWT Token Not Working**: Ensure you add the `Authorization` header with the token for protected routes.
- **Permission Denied**: Check if the user has the required permissions (e.g., admin for product deletion).

---

### **Future Enhancements**
- Add support for product categories.
- Implement search and filtering for products.
- Add order history and invoice generation.

---

### **Contributing**

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

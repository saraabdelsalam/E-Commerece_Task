
## Project Overview
This project implements a RESTful API using Flask for a simple e-commerce application. It includes user registration, authentication, and access control features, along with basic database operations.

## Features
- User registration with input validation and hashed passwords.
- Login functionality with JWT authentication.
- Role-based access control for admin-only and user-accessible pages.
- Public visitor endpoint.
- Database schema designed with SQLAlchemy, including relationships between Users, Products, Orders, and OrderItems.
  
## Endpoints
1. **User Registration (/register)**
   - Allows new users to register by providing first name, last name, email, phone number, and password, user role.
   - Data validation applied before adding new users
   - Passwords are securely hashed before saving.

2. **Login (/login)**
   - Authenticates users and provides a JWT token for authorized access.

3. **Admin-Only Page (/systemAdmin)**
   - Restricted to admin users, returns `hello_{admin_name}`.

4. **All Users Page (/users)**
   - Accessible to all users, including admin, and returns `hello_{username}`.

5. **Visitor Page (/visitors)**
   - Accessible to everyone, including unauthenticated users, and returns `hello_visitor`.

## Database Schema
- **Users Table**: Stores user information such as first name, last name, email, password, and user role.
- **Products Table**: Stores product details.
- **Orders Table**: Stores order information.
- **OrderItems Table**: Stores information about items in each order.

### ER Diagram
![alt text](https://github.com/saraabdelsalam/E-Commerece_Task/blob/main/E-Commerece_ER.png)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url
   cd your-repo-directory
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Modify the database URI in `config.py` with your database configuration.
   - Run the following command to create the tables:
     ```bash
     python -m models.py
     ```

4. Run the Flask application:
   ```bash
   flask run
   ```

5. Access the application on `http://127.0.0.1:5000/`.

## API Documentation
- You can view the full API documentation using Postman. Import the Postman collection from `api_docs/postman_collection.json` (if provided) for details about request parameters, responses, and error messages for each endpoint.

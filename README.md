
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
   git clone https://github.com/saraabdelsalam/E-Commerece_Task.git
   cd your-repo-directory
   ```

2. Install dependencies:
   prerequisite: install python 3.12.7 first / install python extension in case using vs code
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Modify the database URI in `config.py` with your database configuration.
   - Run the following command to create the tables:
     ```bash
     python -m Repository.init_db
     ```
     note: if an error appears for flask-sqlalchemy moduleNotfound then use this command
          ```bash
     pip install flask-sqlalchemy
     ```
5. Run the Flask application:
   ```bash
   flask run
   ```

6. Access the application on `http://127.0.0.1:5000/`.

## API Documentation
- You can view the API documentation for register endpoint using Postman. https://documenter.getpostman.com/view/30839468/2sAXxPAYWW#87e1101d-3018-4c7b-ba7d-66d6b2c8f718 for details about request parameters, responses, and error messages for the endpoint.

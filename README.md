# ZeBrands Product Catalog Solution

This repository contains a minimal solution to manage a product catalog for ZeBrands.

The solution is designed with a robust layered architecture, design patterns, and follows Domain-Driven Design (DDD) principles. 

It supports role-based access (admins and anonymous users), notifications, and product usage tracking.

The project includes unit and integration tests and is documented using Swagger/OpenAPI.




# Architecture 

```
+-------------------------------------------+
|                   API                     |
|       (FastAPI + Swagger/OpenAPI)         |
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Application Layer          |
|  (Service handlers, DTOs, API controllers)|
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Domain Layer               |
|   (Entities, Value Objects, Aggregates,   |
|           Domain Services)                |
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Infrastructure Layer       |
|    (Repositories, Data Sources,           |
|     External Service Integrations)        |
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Database                   |
|            (PostgreSQL)                   |
+-------------------------------------------+
```



# Use Cases Supported

- Login: Authenticate a user and return a Bearer token to access protected endpoints.
- Add Users: Add a new user.
- Lis Users: Display all existing users.
- Enable Admin Permissions: Grant admin permissions to a specified user
- Delete User : Remove a specified user from the system

- Create Product: Add a new product to the catalog with SKU, name, price, stock and brand.
- List Products: Display all products in the catalog.
- Update Product: Modify details of an existing product.



# How to Test the API

## 1. User Setup & Authentication

1. **/users/admins (POST)**: Add a new user to the system. 

2. **/auth/login (POST)** : Auth to the system, The response will include a **Bearer token**.  
   ⚠️ **Note:** You only need to copy this token **once**; it will be valid for accessing protected endpoints until it expires.

3. **Use the Bearer token**: Paste the token in the "Authorize" feature in Swagger UI to access protected endpoints.

---

## 2. Product Endpoints

1. **Create Product**: Add a new product to the catalog with SKU, name, price, stock and brand.
2. **List Products**: Display all products in the catalog.
3. **Update Product**: Modify an existing product.


# Future Improvements

- Dedicated Authentication Endpoint: Implement a login endpoint to issue Bearer tokens independently of user creation, improving security, aligning with best practices, and enhancing the developer and user experience.

- OpenTelemetry Implementation for Enhanced Observability: Integrate OpenTelemetry to gain comprehensive visibility into product catalog operations, user interactions, and notifications, enabling detailed tracking, troubleshooting, and performance optimization.

- Increased Use of Constants and Code Parameterization: Refactor code to expand the use of constants and parameters, enhancing flexibility, readability, and ease of maintenance.

- Function Composition Optimization: Refine the structure and composition of functions to enhance modularity and reduce redundancy, fostering a codebase that is more readable, maintainable, and adaptable to future enhancements.

- Adherence to SOLID Principles and Clean Architecture: Improve alignment with SOLID principles and Clean Architecture standards, reinforcing the separation of concerns, improving code scalability, and establishing a robust, maintainable framework that simplifies testing and facilitates long term evolution.

- Improve Testing Coverage: Increase unit and integration test coverage to ensure code reliability and robustness.

- Implement CI/CD Pipeline: Set up a Continuous Integration / Continuous Deployment pipeline to automate testing, building, and deployment, improving efficiency and reducing production errors.


## Email Notifications (AWS SES Sandbox)

This project uses **AWS SES in sandbox mode**, which only allows sending emails to verified addresses.  
**For this test, all admin notification emails are limited to:** `dorianbarbozazebrands@gmail.com`.

⚠️ **Note:** This limitation is only for the sandbox environment.  
In a production SES environment, emails could be sent to any address without restriction.


- **Email User:** `dorianbarbozazebrands@gmail.com`  
- **Password:** dorianbarbozazebrandS1#



# Access the API documentation
- **Local Environment:**  
  Open your browser and go to [http://localhost:8080/docs](http://localhost:8080/docs) 

- **Production Environment (AWS with SES for email notifications):**  
  [http://18.218.17.152:8080/docs](http://18.218.17.152:8080/docs)

# Testing

docker exec -ti technical-test-dorianbarboza-app-1 pytest -v

# Usage
```bash
docker compose up -d
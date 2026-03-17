# CSCE 548 – Project 4 Deployment and System Test

## Student
Nishant Chinnasami

## Project Overview
This project implements a vulnerability tracking system using a layered architecture consisting of a service layer (FastAPI), business logic layer, and data access layer connected to a MySQL database. The API provides endpoints for managing users, systems, vulnerabilities, and scans.

## System Testing

After deploying the API locally, the endpoints were tested using the FastAPI Swagger UI available at:

http://127.0.0.1:8000/docs

The following API operations were tested successfully:

### 1. Create User
POST /users was used to create a new user in the system.

### 2. Get Users
GET /users returned the list of all users stored in the database.

### 3. Update User
PUT /users/{user_id} successfully updated an existing user's information.

### 4. Create System
POST /systems was used to insert a new system record.

### 5. Get Systems
GET /systems returned the list of stored systems.

### 6. Create Vulnerability
POST /vulnerabilities was used to add a vulnerability entry.

### 7. Get Vulnerabilities
GET /vulnerabilities returned all vulnerability records.

These tests confirmed that the service layer, business logic layer, and data access layer were functioning correctly and communicating with the MySQL database.

## Screenshots

The following screenshots were captured during testing and will be included in the final PDF submission:

- Swagger API homepage showing all endpoints
- POST /users successful request and response
- GET /users successful response
- GET /users/{user_id} successful response
- PUT /users/{user_id} successful response
- POST /systems successful request and response
- GET /systems successful response
- POST /vulnerabilities successful request and response
- GET /vulnerabilities successful response
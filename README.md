# CSCE 548 – Vulnerability Tracking System

This repository contains the implementation of a **vulnerability tracking system** developed for **CSCE 548 – Building Secure Software (Spring 2026)**.

The system manages information about **users, systems, vulnerabilities, and scan records** using a layered architecture. A **FastAPI REST service** interacts with a **MySQL database** through a business layer and data access layer.

---

# Architecture

The project follows a **3-layer architecture**:

**Service Layer**
- FastAPI REST API
- Handles HTTP requests and responses

**Business Layer**
- Contains application logic
- Validates and processes data before database access

**Data Access Layer**
- DAO classes interact directly with the MySQL database
- Executes SQL queries and returns results

---

# Technologies Used

- Python
- FastAPI
- MySQL Community Server
- mysql-connector-python
- Uvicorn
- Git
- GitHub

---

# Project Structure

```
csce548-db
│
├── sql
│   ├── create_tables.sql
│   └── insert_data.sql
│
├── src
│   ├── service.py
│   ├── app.py
│   ├── db.py
│   │
│   ├── business
│   │   └── business.py
│   │
│   └── data
│       ├── users_dao.py
│       ├── systems_dao.py
│       ├── vulnerabilities_dao.py
│       └── scans_dao.py
│
├── project4_deployment_and_system_test.pdf
└── README.md
```

---

# Database Setup

Start your MySQL server and run the SQL scripts:

```
sql/create_tables.sql
sql/insert_data.sql
```

These scripts will:
- Create the vulnerability tracking database
- Create tables for users, systems, vulnerabilities, and scans
- Insert sample data

---

# Installing Dependencies

Install the required Python packages:

```bash
pip3 install fastapi uvicorn mysql-connector-python
```

---

# Running the API

From the **repository root directory**, start the FastAPI server:

```bash
uvicorn src.service:app --reload --port 8000
```

The server will run at:

```
http://127.0.0.1:8000
```

---

# API Documentation

Interactive Swagger documentation is available at:

```
http://127.0.0.1:8000/docs
```

This interface allows testing all API endpoints including:

- Users
- Systems
- Vulnerabilities
- Scans

---

# Deployment and System Testing

Deployment instructions and system testing screenshots are included in the following document:

```
project4_deployment_and_system_test.pdf
```

This document demonstrates that the API endpoints were successfully tested using Swagger UI.

---

# Author

Nishant Chinnasami  
CSCE 548 – Building Secure Software  
Spring 2026
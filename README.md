# CSCE 548 Project 1 – Vulnerability Tracking System

This project is a simple security vulnerability tracking system built for CSCE 548 Project 1.

The database stores information about users, systems, vulnerabilities, and scan results. A MySQL database is used along with a Python console application to demonstrate basic CRUD operations and data retrieval.

## Technologies Used
- MySQL Community Server
- Python
- mysql-connector-python
- GitHub

## Files
- sql/create_tables.sql – Creates database and tables
- sql/insert_data.sql – Inserts sample data
- src/app.py – Python console application
- screenshots/ – Execution and database screenshots

## How to Run
1. Start MySQL server
2. Run SQL scripts:
   - create_tables.sql
   - insert_data.sql
3. Update MySQL password in app.py
4. Run:
   python3 app.py

The console menu allows viewing scan records and adding new users.


CREATE DATABASE IF NOT EXISTS vuln_tracker;
USE vuln_tracker;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE systems (
    system_id INT AUTO_INCREMENT PRIMARY KEY,
    hostname VARCHAR(100),
    ip_address VARCHAR(50),
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES users(user_id)
);

CREATE TABLE vulnerabilities (
    vuln_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150),
    severity VARCHAR(20),
    description TEXT
);

CREATE TABLE scans (
    scan_id INT AUTO_INCREMENT PRIMARY KEY,
    system_id INT,
    vuln_id INT,
    scan_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (system_id) REFERENCES systems(system_id),
    FOREIGN KEY (vuln_id) REFERENCES vulnerabilities(vuln_id)
);

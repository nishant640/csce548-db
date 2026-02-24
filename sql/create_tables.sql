DROP DATABASE IF EXISTS vuln_tracker;
CREATE DATABASE vuln_tracker;
USE vuln_tracker;

CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE systems (
  system_id INT AUTO_INCREMENT PRIMARY KEY,
  hostname VARCHAR(120) NOT NULL,
  ip_address VARCHAR(45) NOT NULL,
  owner_id INT NOT NULL,
  CONSTRAINT uq_system_ip UNIQUE (ip_address),
  CONSTRAINT fk_systems_owner
    FOREIGN KEY (owner_id) REFERENCES users(user_id)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE vulnerabilities (
  vuln_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  severity VARCHAR(10) NOT NULL,
  description TEXT,
  CONSTRAINT chk_severity
    CHECK (severity IN ('LOW','MEDIUM','HIGH','CRITICAL'))
);

CREATE TABLE scans (
  scan_id INT AUTO_INCREMENT PRIMARY KEY,
  system_id INT NOT NULL,
  vuln_id INT NOT NULL,
  scan_date DATE NOT NULL,
  status VARCHAR(20) NOT NULL,
  CONSTRAINT chk_status
    CHECK (status IN ('OPEN','IN_PROGRESS','RESOLVED','FALSE_POSITIVE')),
  CONSTRAINT fk_scans_system
    FOREIGN KEY (system_id) REFERENCES systems(system_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_scans_vuln
    FOREIGN KEY (vuln_id) REFERENCES vulnerabilities(vuln_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);
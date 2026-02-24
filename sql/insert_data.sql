USE vuln_tracker;

-- USERS (10)
INSERT INTO users (name,email) VALUES
('Alice','alice@test.com'),
('Bob','bob@test.com'),
('Carol','carol@test.com'),
('Dave','dave@test.com'),
('Eve','eve@test.com'),
('Frank','frank@test.com'),
('Grace','grace@test.com'),
('Heidi','heidi@test.com'),
('Ivan','ivan@test.com'),
('Judy','judy@test.com');

-- SYSTEMS (10)
INSERT INTO systems (hostname,ip_address,owner_id) VALUES
('srv01','10.0.0.1',1),
('srv02','10.0.0.2',2),
('srv03','10.0.0.3',3),
('srv04','10.0.0.4',4),
('srv05','10.0.0.5',5),
('srv06','10.0.0.6',6),
('srv07','10.0.0.7',7),
('srv08','10.0.0.8',8),
('srv09','10.0.0.9',9),
('srv10','10.0.0.10',10);

-- VULNERABILITIES (10)
INSERT INTO vulnerabilities (title,severity,description) VALUES
('SQL Injection','HIGH','classic sqli'),
('XSS','MEDIUM','cross site scripting'),
('Open Port','LOW','unused port'),
('Weak Password','CRITICAL','password policy'),
('Outdated SSL','HIGH','old tls'),
('Missing Patch','MEDIUM','patch missing'),
('Default Creds','CRITICAL','defaults'),
('Directory Listing','LOW','apache'),
('RCE','CRITICAL','remote exec'),
('CSRF','MEDIUM','csrf bug');

-- SCANS (20)
INSERT INTO scans (system_id,vuln_id,scan_date,status) VALUES
(1,1,'2025-01-01','OPEN'),
(1,2,'2025-01-02','RESOLVED'),
(2,3,'2025-01-03','OPEN'),
(2,4,'2025-01-04','IN_PROGRESS'),
(3,5,'2025-01-05','OPEN'),
(3,6,'2025-01-06','RESOLVED'),
(4,7,'2025-01-07','OPEN'),
(4,8,'2025-01-08','RESOLVED'),
(5,9,'2025-01-09','IN_PROGRESS'),
(5,10,'2025-01-10','OPEN'),
(6,1,'2025-01-11','OPEN'),
(6,2,'2025-01-12','RESOLVED'),
(7,3,'2025-01-13','OPEN'),
(7,4,'2025-01-14','RESOLVED'),
(8,5,'2025-01-15','OPEN'),
(8,6,'2025-01-16','RESOLVED'),
(9,7,'2025-01-17','OPEN'),
(9,8,'2025-01-18','RESOLVED'),
(10,9,'2025-01-19','OPEN'),
(10,10,'2025-01-20','RESOLVED');
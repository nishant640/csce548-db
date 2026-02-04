USE vuln_tracker;

INSERT INTO users (name, email) VALUES
('Alice Smith','alice@test.com'),
('Bob Jones','bob@test.com'),
('Charlie Lee','charlie@test.com'),
('David Kim','david@test.com'),
('Emma Brown','emma@test.com');

INSERT INTO systems (hostname, ip_address, owner_id) VALUES
('web-server','192.168.1.10',1),
('db-server','192.168.1.11',2),
('mail-server','192.168.1.12',3),
('app-server','192.168.1.13',4),
('backup-server','192.168.1.14',5);

INSERT INTO vulnerabilities (title, severity, description) VALUES
('SQL Injection','High','Injection vulnerability'),
('XSS','Medium','Cross site scripting'),
('Open Port','Low','Unnecessary open port'),
('Weak Password','High','Password too weak'),
('Outdated Software','Medium','Needs patching');

-- 40+ scan records
INSERT INTO scans (system_id, vuln_id, scan_date, status) VALUES
(1,1,'2026-02-01','Open'),
(1,2,'2026-02-01','Closed'),
(1,3,'2026-02-01','Open'),
(2,1,'2026-02-01','Open'),
(2,2,'2026-02-01','Closed'),
(2,3,'2026-02-01','Closed'),
(3,4,'2026-02-01','Open'),
(3,5,'2026-02-01','Closed'),
(4,1,'2026-02-01','Open'),
(4,2,'2026-02-01','Open'),
(5,3,'2026-02-01','Closed'),
(5,4,'2026-02-01','Open'),

(1,1,'2026-02-02','Closed'),
(2,2,'2026-02-02','Open'),
(3,3,'2026-02-02','Open'),
(4,4,'2026-02-02','Closed'),
(5,5,'2026-02-02','Open'),
(1,2,'2026-02-02','Closed'),
(2,3,'2026-02-02','Closed'),
(3,1,'2026-02-02','Open'),

(1,3,'2026-02-03','Open'),
(2,4,'2026-02-03','Open'),
(3,5,'2026-02-03','Closed'),
(4,1,'2026-02-03','Closed'),
(5,2,'2026-02-03','Open'),
(1,4,'2026-02-03','Closed'),
(2,5,'2026-02-03','Open'),
(3,2,'2026-02-03','Closed'),
(4,3,'2026-02-03','Open'),
(5,1,'2026-02-03','Closed');

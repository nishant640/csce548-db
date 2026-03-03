"""
Service Layer (FastAPI)
Hosts REST endpoints that call the business layer.

HOW TO RUN LOCALLY (Mac / VS Code):
1) Install deps:
   pip3 install fastapi uvicorn mysql-connector-python
2) Start server from repo root:
   uvicorn src.service:app --reload --port 8000
3) Open docs:
   http://127.0.0.1:8000/docs

HOSTING (example):
- Render, Railway, Fly.io, or an EC2 instance can run this with a startup command like:
  uvicorn src.service:app --host 0.0.0.0 --port 8000
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from src.business.business import (
    # users
    add_user, fetch_user, fetch_all_users, edit_user, remove_user,
    # systems
    add_system, fetch_system, fetch_all_systems, edit_system, remove_system,
    # vulnerabilities
    add_vulnerability, fetch_vulnerability, fetch_all_vulnerabilities, edit_vulnerability, remove_vulnerability,
    # scans
    add_scan, fetch_scan, fetch_all_scans, edit_scan, remove_scan
)

app = FastAPI(title="CSCE 548 Project 2 Services")

# ---- CORS (needed for Project 3 frontend on port 5500) ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------- Request Models -----------

class UserIn(BaseModel):
    name: str
    email: str

class SystemIn(BaseModel):
    hostname: str
    ip_address: str
    owner_id: int

class VulnerabilityIn(BaseModel):
    title: str
    severity: str
    description: str | None = None

class ScanIn(BaseModel):
    system_id: int
    vuln_id: int
    scan_date: str  # "YYYY-MM-DD"
    status: str

# ----------- USERS -----------

@app.get("/users")
def api_get_users(limit: Optional[int] = Query(default=None, ge=1)):
    rows = fetch_all_users()
    if limit:
        return rows[:limit]
    return rows

@app.get("/users/{user_id}")
def api_get_user(user_id: int):
    row = fetch_user(user_id)
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    return row

@app.post("/users")
def api_create_user(payload: UserIn):
    new_id = add_user(payload.name, payload.email)
    return {"user_id": new_id}

@app.put("/users/{user_id}")
def api_update_user(user_id: int, payload: UserIn):
    ok = edit_user(user_id, payload.name, payload.email)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found")
    return {"updated": True}

@app.delete("/users/{user_id}")
def api_delete_user(user_id: int):
    ok = remove_user(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": True}

# ----------- SYSTEMS -----------

@app.get("/systems")
def api_get_systems(limit: Optional[int] = Query(default=None, ge=1)):
    rows = fetch_all_systems()
    if limit:
        return rows[:limit]
    return rows

@app.get("/systems/{system_id}")
def api_get_system(system_id: int):
    row = fetch_system(system_id)
    if not row:
        raise HTTPException(status_code=404, detail="System not found")
    return row

@app.post("/systems")
def api_create_system(payload: SystemIn):
    new_id = add_system(payload.hostname, payload.ip_address, payload.owner_id)
    return {"system_id": new_id}

@app.put("/systems/{system_id}")
def api_update_system(system_id: int, payload: SystemIn):
    ok = edit_system(system_id, payload.hostname, payload.ip_address, payload.owner_id)
    if not ok:
        raise HTTPException(status_code=404, detail="System not found")
    return {"updated": True}

@app.delete("/systems/{system_id}")
def api_delete_system(system_id: int):
    ok = remove_system(system_id)
    if not ok:
        raise HTTPException(status_code=404, detail="System not found")
    return {"deleted": True}

# ----------- VULNERABILITIES -----------

@app.get("/vulnerabilities")
def api_get_vulns(limit: Optional[int] = Query(default=None, ge=1)):
    rows = fetch_all_vulnerabilities()
    if limit:
        return rows[:limit]
    return rows

@app.get("/vulnerabilities/{vuln_id}")
def api_get_vuln(vuln_id: int):
    row = fetch_vulnerability(vuln_id)
    if not row:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    return row

@app.post("/vulnerabilities")
def api_create_vuln(payload: VulnerabilityIn):
    new_id = add_vulnerability(payload.title, payload.severity, payload.description)
    return {"vuln_id": new_id}

@app.put("/vulnerabilities/{vuln_id}")
def api_update_vuln(vuln_id: int, payload: VulnerabilityIn):
    ok = edit_vulnerability(vuln_id, payload.title, payload.severity, payload.description)
    if not ok:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    return {"updated": True}

@app.delete("/vulnerabilities/{vuln_id}")
def api_delete_vuln(vuln_id: int):
    ok = remove_vulnerability(vuln_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    return {"deleted": True}

# ----------- SCANS -----------

@app.get("/scans")
def api_get_scans(limit: Optional[int] = Query(default=None, ge=1)):
    rows = fetch_all_scans()
    if limit:
        return rows[:limit]
    return rows

@app.get("/scans/{scan_id}")
def api_get_scan(scan_id: int):
    row = fetch_scan(scan_id)
    if not row:
        raise HTTPException(status_code=404, detail="Scan not found")
    return row

@app.post("/scans")
def api_create_scan(payload: ScanIn):
    new_id = add_scan(payload.system_id, payload.vuln_id, payload.scan_date, payload.status)
    return {"scan_id": new_id}

@app.put("/scans/{scan_id}")
def api_update_scan(scan_id: int, payload: ScanIn):
    ok = edit_scan(scan_id, payload.system_id, payload.vuln_id, payload.scan_date, payload.status)
    if not ok:
        raise HTTPException(status_code=404, detail="Scan not found")
    return {"updated": True}

@app.delete("/scans/{scan_id}")
def api_delete_scan(scan_id: int):
    ok = remove_scan(scan_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Scan not found")
        return {"deleted": True}
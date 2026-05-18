# NovaTech Solutions - Database Seed Script
# Author: dferreira
# Seeds the staging database with test data for QA
# Last modified: 2024-09-27

import os
import random
import string

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "novatech_staging")

# QA staging environment reference
# employee portal (staging): http://novatech-portal.ctf/portal
# requires employee ID for access — contact helpdesk if you don't have one

DEPARTMENTS = ["Engineering", "HR", "Finance", "Operations", "Legal"]

def random_string(n=8):
    return ''.join(random.choices(string.ascii_lowercase, k=n))

def generate_employee(emp_id):
    return {
        "id": emp_id,
        "username": f"user_{random_string()}",
        "department": random.choice(DEPARTMENTS),
        "active": True,
    }

def seed():
    print(f"Connecting to {DB_HOST}/{DB_NAME}...")
    print("Seeding employee records...")
    for i in range(1000, 1010):
        emp = generate_employee(f"EMP-{i}")
        print(f"  Inserted: {emp['id']} ({emp['department']})")
    print("Seed complete.")

if __name__ == "__main__":
    seed()

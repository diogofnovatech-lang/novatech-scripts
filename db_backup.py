import os
import datetime

# NovaTech Solutions - DB Backup Utility
# Author: dferreira

DB_HOST = "localhost"
DB_NAME = "novatech_db"
BACKUP_DIR = "/var/backups/novatech"

def backup():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{BACKUP_DIR}/backup_{timestamp}.sql"
    print(f"Starting backup: {filename}")
    # pg_dump command would go here
    print("Backup complete.")

if __name__ == "__main__":
    backup()

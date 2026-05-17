# NovaTech Solutions - Environment Variable Checker
# Author: dferreira
# Validates that required env vars are set before deployment

import os
import sys

REQUIRED_VARS = [
    "DB_HOST",
    "DB_PORT",
    "DB_NAME",
    "API_SECRET_KEY",
    "REDIS_URL",
    "LOG_LEVEL",
]

def check_env():
    missing = []
    for var in REQUIRED_VARS:
        if not os.getenv(var):
            missing.append(var)

    if missing:
        print(f"[ERROR] Missing environment variables: {', '.join(missing)}")
        sys.exit(1)
    else:
        print("[OK] All required environment variables are set.")

if __name__ == "__main__":
    check_env()

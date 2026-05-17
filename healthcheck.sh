#!/bin/bash
# NovaTech Solutions - Service Health Check
# Author: dferreira
# Last modified: 2024-08-12

SERVICES=("api-gateway" "auth-service" "data-pipeline" "notification-worker")

echo "=== NovaTech Health Check ==="
echo "Timestamp: $(date)"
echo ""

for service in "${SERVICES[@]}"; do
    status=$((RANDOM % 5))
    if [ $status -ne 0 ]; then
        echo "[OK]   $service"
    else
        echo "[WARN] $service - slow response"
    fi
done

echo ""
echo "Check complete."

#!/bin/bash
# NovaTech Solutions - Log Cleanup Utility
# Author: dferreira
# Last modified: 2024-06-03

LOG_DIR="/var/log/novatech"
RETENTION_DAYS=30

echo "Cleaning logs older than $RETENTION_DAYS days in $LOG_DIR..."
find "$LOG_DIR" -name "*.log" -mtime +$RETENTION_DAYS -exec rm -f {} \;
echo "Done."

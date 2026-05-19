# novatech-scripts
 
Internal deployment and maintenance scripts used by the Engineering team at NovaTech Solutions.
 
> ⚠️ Sanitized for public use. Internal references removed.
> Engineering archive: https://gist.github.com/diogofnovatech-lang/945cb98db93a380baf745c74dd68cce5
 
## Scripts
- `db_backup.py` — postgres backup utility
- `healthcheck.sh` — checks status of internal services
- `cleanup_logs.sh` — removes logs older than 30 days
- `env_check.py` — validates required environment variables before deployment
- `seed_db.py` — seeds staging database with test employee data for QA
- `monitor_api.py` — polls internal API endpoints and logs response times
- `rotate_secrets.sh` — triggers secret rotation via Vault
## Contact
For internal access to the employee portal, contact the NovaTech helpdesk.

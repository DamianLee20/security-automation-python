# Security Automation with Python 🛡️

This project automates log parsing, anomaly detection, and alerting using Python. It showcases how SOC analysts can reduce manual work and improve threat visibility through scripting.

## Features

- 🧾 Log Parsing (Regex-based)
- ⚠️ Anomaly Detection (e.g., failed logins, critical errors)
- 🔁 Automated Workflows
- 📬 Alerting Simulation
- 📊 Output to JSON for integration

## How to Run

```bash
source venv/bin/activate
bash scripts/workflow_example.sh

2025-07-17 10:23:12 INFO User login successful
2025-07-17 10:25:48 CRITICAL Failed login attempt for user admin


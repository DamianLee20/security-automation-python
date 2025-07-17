#!/bin/bash
echo "[*] Starting automated security workflow..."

python3 scripts/parse_logs.py
python3 scripts/detect_anomalies.py
python3 scripts/send_alerts.py

echo "[*] Workflow complete."


import json

with open('output/parsed_logs.json') as f:
    logs = json.load(f)

anomalies = [log for log in logs if "failed login" in log['msg'].lower() or log['level'] == "CRITICAL"]

with open('output/anomalies_report.json', 'w') as f:
    json.dump(anomalies, f, indent=4)

print(f"[!] Detected {len(anomalies)} anomalies.")


import json

with open('output/anomalies_report.json') as f:
    anomalies = json.load(f)

if not anomalies:
    print("[*] No anomalies found.")
else:
    for a in anomalies:
        print(f"[ALERT] {a['timestamp']} - {a['msg']}")


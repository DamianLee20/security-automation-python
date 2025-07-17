import re, json

logfile = 'logs/sample_logs.log'
parsed_output = []

pattern = re.compile(r'(?P<timestamp>[\d\-: ]+)\s+(?P<level>\w+)\s+(?P<msg>.*)')

with open(logfile, 'r') as f:
    for line in f:
        match = pattern.match(line)
        if match:
            parsed_output.append(match.groupdict())

with open('output/parsed_logs.json', 'w') as f:
    json.dump(parsed_output, f, indent=4)

print(f"[+] Parsed {len(parsed_output)} log lines.")


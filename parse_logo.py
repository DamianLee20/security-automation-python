import re, json

logfile = 'logs/sample_logs.log'
parsed_output = []

pattern = re.compile(r'(?P<timestamp>[\d\-: ]+)\s+(?P<level>\w+)\s+(?P<msg>.*)')

with open(logfile, 'r') as f:
    for line in f:
        print(f"Processing: {line.strip()}")  # Debug line
        match = pattern.match(line)
        if match:
            print(f"Matched: {match.groupdict()}")  # Debug line
            parsed_output.append(match.groupdict())
        else:
            print("No match found.")  # Debug line

with open('output/parsed_logs.json', 'w') as f:
    json.dump(parsed_output, f, indent=4)

print(f"[+] Parsed {len(parsed_output)} log lines.")


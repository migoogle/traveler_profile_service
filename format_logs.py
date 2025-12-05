import json

with open('logs.json') as f:
    try:
        logs = json.load(f)
    except json.JSONDecodeError:
        print("Could not decode logs.json. It might be empty or malformed.")
        exit()

for log in logs:
    timestamp = log.get('timestamp', '')
    text_payload = log.get('textPayload', '')
    
    if text_payload:
        try:
            # Try to parse the text_payload as JSON
            payload = json.loads(text_payload)
            # If successful, pretty-print it
            text_payload = json.dumps(payload, indent=2)
        except (json.JSONDecodeError, TypeError):
            # If it's not a JSON string, just use it as is
            pass
        
        print(f"{timestamp}\n{text_payload}\n")
import os
import json

# Path to mandirs.json
json_path = os.path.join("content", "mandirs", "mandirs.json")

# Load JSON data
with open(json_path, "r") as f:
    mandirs = json.load(f)

# Check existence of each file
print("Checking mandir images:\n")

missing = []
for mandir in mandirs:
    url = mandir["url"]
    if os.path.exists(url):
        pass
    else:
        missing.append(url)

if missing:
    print("Missing mandir images:")
    for url in missing:
        print(url)
else:
    print("All mandir images are present.")
        


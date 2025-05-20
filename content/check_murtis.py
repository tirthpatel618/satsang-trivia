import os
import json

json_path = os.path.join("content", "murtis", "murtis.json")

with open(json_path, "r") as f:
    murtis = json.load(f)

print("Checking murti images:\n")

missing = []
for murti in murtis:
    url = murti["url"]
    if os.path.exists(url):
        pass
    else:
        missing.append(url)

if missing:
    print("Missing murti images:")
    for url in missing:
        print(url)
else:
    print("All murti images are present.")
        


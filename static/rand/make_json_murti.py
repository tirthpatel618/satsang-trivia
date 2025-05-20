import json

mandirs = [
    "Toronto, Canada", "Chicago, USA", "Robbinsville, USA", "Houston, USA", "Edison, USA", "Atlanta, USA", "Los Angeles, USA",
    "London, UK", "Nairobi, Kenya", "Ahmedabad, Gujarat",  "Atladara, Gujarat", "Bhadra, Gujarat",
    "Bharuch, Gujarat",  "Bochasan, Gujarat", "Delhi, India", 
     "Gadhada, Gujarat", "Gondal, Gujarat",
    "Mahuva, Gujarat", "Mumbai, Maharashtra", 
    "Nashik, Maharashtra", "Pune, Maharashtra", "Rajkot, Gujarat", "Sankari, Gujarat", "Sarangpur, Gujarat",
    "Silvassa, Gujarat", "Surat, Gujarat",  "Tithal, Gujarat", "Abu Dhabi, UAE"
]

khand_info = {
    "Akshar Purushottam": "ap",
    "Ghanshyam Maharaj": "g"
}

murti_entries = []

count = 1
for mandir in mandirs:
    city = mandir.split(",")[0].strip()
    base = city.lower().replace(" ", "_")
    for khand, suffix in khand_info.items():
        murti_entries.append({
            "id": count,
            "place": city,
            "khand": khand,
            "url": f"content/murtis/{base}_{suffix}.jpg"
        })
        count += 1

with open("murtis.json", "w") as json_file:
    json.dump(murti_entries, json_file, indent=4)

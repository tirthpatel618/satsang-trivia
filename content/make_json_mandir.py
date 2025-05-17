import json

mandirs = [
    "Toronto, Canada", "Chicago, USA", "Robbinsville, USA", "Houston, USA", "Edison, USA", "Atlanta, USA", "Los Angeles, USA",
    "Neasden, UK", "Nairobi, Kenya", "Sydney, Australia", "Ahmedabad, Gujarat", "Anand, Gujarat", "Atladara, Gujarat", "Bhadra, Gujarat",
    "Bharuch, Gujarat", "Bhavnagar, Gujarat", "Bochasan, Gujarat", "Bodeli, Gujarat", "Delhi, India", "Dhari, Gujarat", "Dholka, Gujarat",
    "Dhule, Maharashtra", "Gadhada, Gujarat", "Gandhinagar, Gujarat", "Godhra, Gujarat", "Gondal, Gujarat", "Himmatnagar, Gujarat",
    "Jaipur, Rajasthan", "Jalandhar, Punjab", "Jamnagar, Gujarat", "Junagadh, Gujarat", "Kolkata, West Bengal", "Limbdi, Gujarat",
    "Mahelav, Gujarat", "Mahesana, Gujarat", "Mahuva, Gujarat", "Mumbai, Maharashtra", "Nadiad, Gujarat", "Nagpur, Maharashtra",
    "Nashik, Maharashtra", "Navsari, Gujarat", "Pune, Maharashtra", "Rajkot, Gujarat", "Sankari, Gujarat", "Sarangpur, Gujarat",
    "Silvassa, Gujarat", "Surat, Gujarat", "Surendranagar, Gujarat", "Tithal, Gujarat", "Abu Dhabi, UAE"
]



mandir_entries = []

count = 1
for mandir in mandirs:
    city = mandir.split(",")[0].strip()
    base = city.lower().replace(" ", "_")
    mandir_entries.append({
        "id": count,
        "place": city,
        "url": f"content/mandirs/{base}.jpg"
    })
    count += 1

with open("mandirs.json", "w") as json_file:
    json.dump(mandir_entries, json_file, indent=4)

import os
import time
from requests import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

cities = [
    "Toronto, Canada", "Chicago, USA", "Robbinsville, USA", "Houston, USA", "Edison, USA", "Atlanta, USA", "Los Angeles, USA",
    "Neasden, UK", "Nairobi, Kenya", "Sydney, Australia", "Ahmedabad, Gujarat", "Anand, Gujarat", "Atladara, Gujarat", "Bhadra, Gujarat",
    "Bharuch, Gujarat", "Bhavnagar, Gujarat", "Bochasan, Gujarat", "Bodeli, Gujarat", "Delhi, India", "Dhari, Gujarat", "Dholka, Gujarat",
    "Dhule, Maharashtra", "Gadhada, Gujarat", "Gandhinagar, Gujarat", "Godhra, Gujarat", "Gondal, Gujarat", "Himmatnagar, Gujarat",
    "Jaipur, Rajasthan", "Jalandhar, Punjab", "Jamnagar, Gujarat", "Junagadh, Gujarat", "Kolkata, West Bengal", "Limbdi, Gujarat",
    "Mahelav, Gujarat", "Mahesana, Gujarat", "Mahuva, Gujarat", "Mumbai, Maharashtra", "Nadiad, Gujarat", "Nagpur, Maharashtra",
    "Nashik, Maharashtra", "Navsari, Gujarat", "Pune, Maharashtra", "Rajkot, Gujarat", "Sankari, Gujarat", "Sarangpur, Gujarat",
    "Silvassa, Gujarat", "Surat, Gujarat", "Surendranagar, Gujarat", "Tithal, Gujarat", "Abu Dhabi, UAE"
]
images_per_city = 5
download_folder = "mandirs"

def fetch_image_links(query, max_links):
    query = quote(query)
    url = f"https://www.google.com/search?tbm=isch&q={query}"
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    img_tags = soup.find_all("img")
    links = []

    for img in img_tags:
        src = img.get("src")
        if src and src.startswith("http"):
            links.append(src)
        if len(links) >= max_links:
            break
    return links

def download_images(city, urls):
    city_dir = os.path.join(download_folder, city.replace(" ", "_"))
    os.makedirs(city_dir, exist_ok=True)

    for i, url in enumerate(urls):
        try:
            img_data = requests.get(url, timeout=5).content
            with open(os.path.join(city_dir, f"{city}_{i+1}.jpg"), "wb") as f:
                f.write(img_data)
            print(f"✔️ {city}_{i+1}.jpg downloaded")
        except Exception as e:
            print(f"❌ Failed to download {url}: {e}")

def main():
    os.makedirs(download_folder, exist_ok=True)
    for city in cities:
        print(f"\n🔍 Scraping images for: {city}")
        query = f"BAPS temple {city}"
        urls = fetch_image_links(query, images_per_city)
        download_images(city, urls)
        time.sleep(2)  # Pause to reduce chance of being blocked

if __name__ == "__main__":
    main()

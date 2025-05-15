import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# Create output directory
os.makedirs('murti_darshan_images', exist_ok=True)

# Load mandir names from file
with open('mandirs.txt', 'r') as f:
    mandirs = [line.strip() for line in f if line.strip() and not line.endswith(':')]

# Helper function to sanitize city name for filenames
def sanitize_city(city):
    return city.lower().replace(' ', '_')

for mandir in mandirs:
    city = mandir.split(',')[0].strip()
    city_slug = city.replace(" ", "")
    url = f'https://www.baps.org/Global-Network/North-America/{city_slug}/Murti-Darshan.aspx'

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            raise Exception(f"Status {response.status_code}")
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        
        count = 1
        for img in img_tags:
            img_src = img.get('src')
            if img_src and img_src.lower().endswith('.jpg'):
                img_url = urljoin(url, img_src)
                img_name = f"{sanitize_city(city)}_{count}.jpg"
                save_path = os.path.join('murti_darshan_images', img_name)

                img_response = requests.get(img_url, headers=headers, timeout=10)
                if img_response.status_code == 200:
                    with open(save_path, 'wb') as f:
                        f.write(img_response.content)
                    print(f'Downloaded: {img_name}')
                    count += 1
                else:
                    print(f'Failed to download image from {img_url}')
    except Exception as e:
        print(f"Error processing {city}: {e}")

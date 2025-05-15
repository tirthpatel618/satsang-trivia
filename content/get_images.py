import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://www.baps.org/Global-Network/North-America/Toronto/Murti-Darshan.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

os.makedirs('murti_darshan_images', exist_ok=True)

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

img_tags = soup.find_all('img')

for img in img_tags:
    img_src = img.get('src')
    if img_src:
        img_url = urljoin(url, img_src)
        img_name = os.path.basename(img_url)
        img_response = requests.get(img_url, headers=headers)
        if img_response.status_code == 200:
            with open(os.path.join('murti_darshan_images', img_name), 'wb') as f:
                f.write(img_response.content)
            print(f'Downloaded: {img_name}')
        else:
            print(f'Failed to download: {img_name}')

#helo

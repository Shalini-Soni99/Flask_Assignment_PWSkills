
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os
save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
query = "KV No.1 raipur"
response = requests.get(f"https://www.google.com/search?q={query}&sca_esv=8a5f3c529fc99551&sxsrf=AHTn8zpPJBvJfvrgjDNNKFGiEdXKsGIOFA:1740069787630&source=hp&biw=1536&bih=730&ei=m1u3Z-nYJJ3F1e8PvPKoSA&iflsig=ACkRmUkAAAAAZ7dpq3HBqQ_bWKvTqwEOwZ1YCoa2tWHK&oq=elon+&gs_lp=EgNpbWciBWVsb24gKgIIADIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzIOEAAYgAQYsQMYgwEYigUyCxAAGIAEGLEDGIMBMggQABiABBixAzILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQNIgxNQAFigB3AAeACQAQCYAdMCoAGrCaoBBzAuMi4yLjG4AQPIAQD4AQGKAgtnd3Mtd2l6LWltZ5gCBaAC2gnCAgcQIxgnGMkCwgIFEAAYgASYAwCSBwcwLjIuMi4xoAeLGw&sclient=img&udm=2")
soup = BeautifulSoup(response.content,'html.parser')
image_tags = soup.find_all("img") 
del image_tags[0]
for i in image_tags:
    images_url = i['src']
    image_data = requests.get(images_url).content 
    with open(os.path.join(save_dir, f"{query}_{image_tags.index(i)}.jpg"), "wb") as f:
        f.write(image_data)
import requests
from bs4 import BeautifulSoup
import time
import vk_api

req_max=500

list_photo_url = []

time.sleep(60/req_max)
url = f"https://vk.com/album269583634_000"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

data = soup.find_all("div", class_="photos_row")
for i in data:
    photo_url = "https://vk.com/" + i.find("a").get("href")
    



    

for photo_url in list_photo_url:
    response = requests.get(photo_url)
    soup = BeautifulSoup(response.text, "lxml")

    url_img = "https://vk.com" + data.find("img", id="pv_photo").get("src")
    print(url_img)
import itertools
import uuid
import vk
import vk_api
import requests, json, time, os
VK_USER_ID = 269583634
VK_TOKEN = "vk1.a.XKvjVSv2BBUhUXhwFepOJqqO1aZgfFcguWmWTHEtT4OZ6fqQfMK-Enl2DYUWNEIhvUn-GuhEZic8H2pRnlqWjQvREkWqaWOUQdbpgsMQnnfAC1ZZ8F72U9QlMNDqH8iirwLQ2jwZPB_EVehcHECS_qlF2PWKaM5RLDGklXWmx8zjckELoE3FuZYlV8TcmpzBpIkwaXR-Fuzcdl3mtFamlw"
APP_TOKEN_KEY = "5b1f91605b1f91605b1f9160c8580e448055b1f5b1f9160388a3f40df429819ee511cc8"
session = vk_api.VkApi(token=VK_TOKEN)
vk = session.get_api()
def get_photo_data(count = 200):
    r = requests.get('https://api.vk.com/method/photos.getAll', params={
		'owner_id': VK_USER_ID, 
		'access_token': VK_TOKEN, 
		'v': 5.78, 
		'album_id': 'saved',
        'count': count,
		'photo_sizes': True
		})
	#write_json(r.json())
#photos = json.load(open('photos.json'))['response']['items']

def get_photo():
    data = get_photo_data()
    count_photo = data
    i = 0
    count = 200
    photos = []
    while i <= count_photo:
        if i != 0:
            data = get_photo_data(offset=i, count=count)
    for files in data["response"]["items"]:
        file_url = files["sizes"][-1]["url"]
    filename = file_url.split("/")[-2]
    photos.append(filename)
    time.sleep(0.1)
    r = requests.get(file_url)
    with open(f"C:\\Users\\User\\Desktop\\parservk\\saved_images\\"+filename+str(i) +'.jpg', 'wb') as file:
        file.write(r.content)
        print(filename, i)

    i = i + 1
    i = count
print(len(photos))

def main():
	get_photo()

if __name__ == "__main__":
	main()
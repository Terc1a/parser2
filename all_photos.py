import requests, json, time, os

VK_USER_ID = 617969371
VK_TOKEN = "vk1.a.qwlHzfzKiDPmqlF0P0LaiNJUGH8Yp5lwBsz-LgmV7KAOBrEqVH1wm2GPl9A4K-tRtxpfiZdWy1yW4fW_I9fZ9NqWZqbi62R5IBQcABl7kePC1E3N5i14H3BnaEicpimBuz-9XGqbSTQVAEP9By5QRlYsddAUWCwr-otkOcHK8gYHelwNa6Mwb8QdLhLEMROe"

def get_photo_data(offset = 0, count = 50):
    api = requests.get("https://api.vk.com/method/photos.getAll", params={
        'owner_id': VK_USER_ID,
        'access_token': VK_TOKEN,
        'offset': offset,
        'count': count,
        'photo_sizes': 0,
        'v': 5.78
    })
    return json.loads(api.text)

def get_photo():
    data = get_photo_data()
    count_photo = data["response"]["count"]
    i = 0
    count = 50
    photos = []
    while i <= count_photo:
        if i != 0:
            data = get_photo_data(offset=i, count=count)
        for files in data["response"]["items"]:
            file_url = files["sizes"][-1]["url"]
            filename = file_url.split("/")[-1]
            photos.append(filename)
            time.sleep(0,1)
            api = requests.get(file_url)

            with open ("images/%s" % filename, "wb") as file:
                file.write(api.content)
        print(i)
        i += count
    print(len(photos))

def main(): 
    get_photo()

if __name__ == "__main__":
	main()
  


import itertools
import uuid
import requests, json, time, os
import json
import urllib.request

ErrorLoger: str

limit = 1000
saveDirectory = "D:/mypyprojects/parservk/nastya_adm/"  # Only '/' !!! Dont use '\'   use full path with .../ in end

VK_USER_ID = 176274843
VK_TOKEN = "vk1.a.XKvjVSv2BBUhUXhwFepOJqqO1aZgfFcguWmWTHEtT4OZ6fqQfMK-Enl2DYUWNEIhvUn-GuhEZic8H2pRnlqWjQvREkWqaWOUQdbpgsMQnnfAC1ZZ8F72U9QlMNDqH8iirwLQ2jwZPB_EVehcHECS_qlF2PWKaM5RLDGklXWmx8zjckELoE3FuZYlV8TcmpzBpIkwaXR-Fuzcdl3mtFamlw"


def write_json(data):
    with open('photos.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_photo_data(offset=0,
                   count=100):  # offset? offset я и просил сделать, чтобы он обновлял, потому шо за раз можно взять ток 1к
    api = requests.get("https://api.vk.com/method/photos.get", params={
        'owner_id': VK_USER_ID,
        'access_token': VK_TOKEN,
        'count': count,
        'album_id': 'saved',
        'photo_sizes': 0,
        'v': 5.131,
        'offset': offset

    })
    write_json(api.json())
    return json.loads(api.text)


def get_photo():
    offset = 0
    i = 0
    data = get_photo_data()
    count_photo = data["response"]["count"]
    while (offset + i) < count_photo:
        data = get_photo_data(offset=offset)
        while i < 100 and (offset + i) < count_photo:

            ##############################---ПОЛОСА ЗАГРУЗКИ---##############################
            print("\r", end="")
            print("{:.1%} ".format((offset + i - 1) / (count_photo + 1)), "[" +
                  "▓" * int(((offset + i) / count_photo) * 50) +
                  "░" * int(49 - int(((offset + i) / count_photo) * 50)) + "] "
                  + str(offset + 1 + i) + "/" + str(count_photo), end="")
            #################################################################################

            try:
                imageURL = data['response']['items'][i]['sizes'][-1]['url']
                saveDirectoryTemp = saveDirectory + str(offset + i + 1) + ".jpg"
                urllib.request.urlretrieve(imageURL, saveDirectoryTemp)
            except:
                # Error log
                pass
            time.sleep(60 / (limit + 1))
            i += 1
        offset += 100
        i = 0

    print("\n", end="")  # что бы работал принт(выход из полосы загрузки)


# file_url = data["response"]["items"]["sizes"][-1]["url"]
# filename = file_url.split("/")[-2]

# photos.append(filename)
# api = requests.get(file_url)

# with open(f"C:\\Users\\User\\Desktop\\parservk\\saved_images_babydosh\\" + filename +str(i)+ '.jpg', "wb") as file:
# 		file.write(api.content)


# while i <= count_photo:
# 	if i != 0:

# 		# print(data["response"]["count"])
# 		# for files in data["response"]["items"]:
# 		# 	file_url = files["sizes"][-1]["url"]
# 		# 	filename = file_url.split("/")[-2]

# 		# 	photos.append(filename)
# 		# 	api = requests.get(file_url)

# 		# 	with open(f"C:\\Users\\User\\Desktop\\parservk\\saved_images_babydosh\\" + filename +str(i)+ '.jpg', "wb") as file:
# 		# 			file.write(api.content)

# 		# 	#with open('images/%s' % filename + '.jpg', "wb") as file:
# 		# 	#	file.write(api.content)
# 		# 	#return(file)
# 		# 	print(filename, i)
# 		# 	i = i + 1
# 		# 	time.sleep(60/(limit+1))
# 		i = 1
# 	else:
# 		i = 1
# print(len(photos))


def main():
    get_photo()


if __name__ == "__main__":
    main()

# print("\r", end="")
#     print("{:.1%} ".format(offset+i / count_photo), "[" + "0" * format(offset+i / count_photo) / 4) +
#           "-" * (49 - format(offset+i / count_photo) / 4)) + "]", end="")
# print("\n", end="")


# 2064

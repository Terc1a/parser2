import itertools
import uuid
import vk_api
import requests, json, time, os

VK_USER_ID = 269583634
VK_TOKEN = "vk1.a.XKvjVSv2BBUhUXhwFepOJqqO1aZgfFcguWmWTHEtT4OZ6fqQfMK-Enl2DYUWNEIhvUn-GuhEZic8H2pRnlqWjQvREkWqaWOUQdbpgsMQnnfAC1ZZ8F72U9QlMNDqH8iirwLQ2jwZPB_EVehcHECS_qlF2PWKaM5RLDGklXWmx8zjckELoE3FuZYlV8TcmpzBpIkwaXR-Fuzcdl3mtFamlw"
APP_TOKEN_KEY = "5b1f91605b1f91605b1f9160c8580e448055b1f5b1f9160388a3f40df429819ee511cc8"
session = vk_api.VkApi(token=VK_TOKEN)
vk = session.get_api()


def write_json(data):
    with open('photos.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


"""def auth_handler():
    

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def main2():
      

    login, password = '+79225511055', '16092000Family'
    vk = vk_api.VkApi(
        login, password,
        # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler
    )

    try:
        vk.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return"""


def get_largest(size_dict):
    # if size_dict['width'] >= size_dict['height']:
    #    return size_dict['width']
    # else:
    #    return size_dict['height']

    weight = {'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 'm': 10, 'x': 20, 'y': 30, 'z': 40, 'w': 50}
    size_dict['type'] = weight[size_dict['type']]
    # return size_dict['type']


def download_photo(url):
    r = requests.get(url, stream=True)
    i = 0
    filename = url.split('/')[-3]
    # print(filename)

    with open(f"D\myprojects\\parservk\\saved_images\\" + filename + str(i) + '.jpg', 'wb') as file:
        file.write(r.content)
        # print(filename, i)

        i = i + 1
    print(len(photos))


def main():
    r = requests.get('https://api.vk.com/method/photos.getAll', params={
        'owner_id': VK_USER_ID,
        'access_token': VK_TOKEN,
        'v': 5.78,
        'album_id': 'saved',
        # 'count': count,
        'photo_sizes': True
    })
    write_json(r.json())


photos = json.load(open('photos.json'))['response']['items']

for photo in photos:
    sizes = photo["sizes"]
    for size in sizes:
        # print(size['type'])
        if size['type'] == 'w':
            url = size['url']
if size['type'] == 'm':
    url = size['url']
    max_size_url = max(sizes)['url']

download_photo(url)
print('------------')
if __name__ == '__main__':
    # main2()
    main()

import vk_api
import requests
my_token = "vk1.a.pq0QEC0QRD7w_6nFs0QtXVyZ69td-fiGTx_dx8CFaseHVB3jmeYXNnHjxWKwoBru3qGcEGcDh5tyHZ1cdAKeJuzjUjP4L7t6kc1W1uCDFG9UBNvFnIzVHPM6xvG9GpmK2R6rLMw__5Q0DjXqiEPk5ghVPXghd9zjSYxKaJDub18AY0KUFih4PdioYsXQDSCGze47eXNiVg6p37oqOlwODQ"
session = vk_api.VkApi(token=my_token)
vk = session.get_api()

method = 'wall.post'
    
version = 5.74
def shitpost(post):  
    data={
     'access_token': my_token,
    'from_group': 1,
      'message': post,
     'signed': 0,
        'v':version}

    r = requests.post('https://api.vk.com/method/wall.post', data).json()
while True:
    shitpost(input())
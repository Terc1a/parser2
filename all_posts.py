from json import json_decode
import vk_api
import requests
from wall_post import my_token
method = 'wall.get'
version = 5.78
session = vk_api.VkApi(my_token)
vk = session.get_api()

def get_post(post):
    data={
    'owner_id': 154717451,
    'access_token' : my_token,
    'v' : 5.78
    }

#url = "https://api.vk.com/method/wall.get?owner_id=120159853&access_token=38fa46d4c0c10bab105c760cc44ed373c0bc6a34405931f34c765ea&v=5.78";

    r = requests.post('https://api.vk.com/method/wall.get?owner_id=154717451&v=5.78', data).json()
    #result = json_decode(file_get_contents(r), true)
import vk_api
import requests
my_token = "vk1.a._vJUsdGP4i50bqb4EEqL-At4vjrdTdZS6bg5XD8vRNwRUmWs7RAUpZX0W_IfGXW0F-en-Fjew6g03uYvsfecgT5GoldtYTLPN584DLNWlIt42cuZZP_nUCN9nJXegi431iO8Bz9MCySdMGxxsVjw4_N3n8TWsrnQHIiaDShIaQ0tWj8MEGNrVoBaCt6AET-hXnLnLpZXFEkJAB3g0aqn4w"
session = vk_api.VkApi(token=my_token)
vk = session.get_api()

def send(msg):
    
    vk.messages.send(user_id = 354409450, message = msg, random_id=0)
   

while True:
    send(input())



   


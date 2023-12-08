import itertools
import uuid
import requests, json, time, os

VK_USER_ID = 617969371
VK_TOKEN = "vk1.a.SRtPrLbcas9QuRtBSHfpgYwKQ_8s9TvaLf210d10XCnJMrqO-38TT3JpTQThbC2MZuIOTUtk060-FErBvolHMbmjuzlu1SCD9lumana43bHbf1R1TvQX730KTiF-zVBmMtMI3RnbmvrTcoEqgzzgGpAZHMYtFUn_UauK2SCfu2T8N-SD7B7AgMmwc_6UoshH_Tzaq6tgKDMc41fvbEOXoA"

def get_photo_data(offset=0, count=50):
	api = requests.get("https://api.vk.com/method/photos.getAll", params={
		'owner_id': VK_USER_ID,
		'access_token': VK_TOKEN,
		'offset': offset,
		'count': count,
		'photo_sizes': 0,
		'v': 5.103
	})
	return json.loads(api.text)

def get_photo():
	data = get_photo_data()
	count_photo = data["response"]["count"]
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
			api = requests.get(file_url)

			with open(f"C:\\Users\\User\\Desktop\\parservk\\images\\" + filename +str(i)+ '.jpg', "wb") as file:
					file.write(api.content)
			
			#with open('images/%s' % filename + '.jpg', "wb") as file:
			#	file.write(api.content)
			#return(file)
			print(filename, i)
			i = i + 1
		i = count
	print(len(photos))

def main():
	get_photo()

if __name__ == "__main__":
	main()



	
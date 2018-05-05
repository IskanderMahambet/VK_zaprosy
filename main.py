import requests

user_id = 'id385236652'
api_url = 'https://api.vk.com/method/'

def get_user(name):
    data = requests.get(api_url+'users.get',{'fields': 'photo_max',
                                             'user_ids':name,
                                             'v':'5.74'})
    return data.json()
print(get_user(user_id))

def get_friends(name):
    data = requests.get(api_url+'friends.get',{'user_id':name,
                                               'v':'5.74'})
    return data.json()

friends1 = set(get_friends('311867269')['response']['items'])
friends2 = set(get_friends('385236652')['response']['items'])
print(friends1&friends2)



friends = friends1 & friends2




for i in friends:
    print(get_user(i))


#user = get_user(user_id)
#url_image = user['response'][0]['photo_max']
#image = requests.get(url_image)
#image_file=open('image.jpg','wb')
#image_file.write(image.content)
#image_file.close()
#print(user)

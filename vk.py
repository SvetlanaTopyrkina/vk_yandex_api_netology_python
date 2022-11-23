import requests
import enum

class VKMethod(enum.Enum):
    users_get = 'users.get'
    photos_get = 'photos.get'
    photos_all_get = 'photos.getAll'

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}
       self.url = 'https://api.vk.com/method/'

   def users_info(self):
       url = self.url + VKMethod.users_get.value
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params}).json()
       if self.check_response(response) == False:
           return [False, ('Не могу подключиться к api VK, причина - {0}'.format(response['error']['error_msg']))]
       return [True, response]

   def get_photos(self):
       url = self.url + VKMethod.photos_get.value

       params = {
           'owner_id': self.id,
           'album_id': 'profile',
           'rev': 0,
           'extended': 1,
           'photo_sizes': 0,
           'count': 20
       }

       response = requests.get(url, params={**self.params, **params}).json()
       if self.check_response(response) == False:
           return [False, ('Не могу подключиться к api VK, причина - {0}'.format(response['error']['error_msg']))]
       return [True, response]

   def get_all_photos(self):
       url = self.url + VKMethod.photos_all_get.value
       params = {'owner_id': self.id}
       response = requests.get(url, params={**self.params, **params}).json()
       if self.check_response(response) == False:
           return [False,('Не могу подключиться к api VK, причина - {0}'.format(response['error']['error_msg']))]
       return [True, response]

   def all_photos(self, vk_reponse):
       album = {}
       for item in vk_reponse['response']['items']:
           name = ''
           if 'likes' in item:
               if item['likes']['count'] in album:
                   name = str(item['likes']['count']) + '_' + str(item['date'])
               else:
                   name = item['likes']['count']
               album.update({name: ''})
           else:
               name = item['date']
           for size in item['sizes']:
               if size['type'] == 'r':
                   album[name] = (size['url'])
       return album

   def check_response(self, response_json):
       if 'error' in response_json:
           return False
       else:
           return True
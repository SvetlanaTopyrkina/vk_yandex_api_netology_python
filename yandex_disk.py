import requests
from urllib.parse import quote

class YandexDisk:

   def __init__(self, access_token):
       self.token = access_token
       self.headers = {'Content-Type': 'application/json; charset=utf-8', 'Accept': 'application/json', 'Authorization': f'OAuth {access_token}'}
       self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

   def create_folder(self, path):
       """Создание папки. \n path: Путь к создаваемой папке."""
       response = requests.put(f'{self.url}?path={path}', headers=self.headers).json()
       if self.check_response(response) == False:
           return ('Не могу создать папку, по причине - {0}'.format(response.json()['error']))
       return True

   def delete_folder(self, path):
       """Удаление папки. \n path: Путь к создаваемой папке."""
       response = requests.delete(f'{self.url}?path={path}', headers=self.headers).json()
       if self.check_response(response) == False:
           return ('Не могу удалить папку, по причине - {0}'.format(response.json()['error']))
       return True

   def upload_file_by_url(self, load, savefile):
       """Загрузка файла."""
       url = self.url + '/upload?path={0}'.format(quote(savefile)) + '&url={0}'.format(quote(load))
       response = requests.post(url, headers=self.headers).json()
       if self.check_response(response) == False:
           return ('Не могу загрузить файл, по причине - {0}'.format(response.json()['error']))
       return True


   def check_folder(self, path):
       """Создание папки. \n path: Путь к создаваемой папке."""
       res = requests.get(f'{self.url}?path={path}', headers=self.headers).json()
       if 'description' in res:
           if res['description'] == 'Resource not found.':
               response = True
           else:
               response = False
       else:
           response = False
       return response

   def check_response(self, response_json):
       if 'error' in response_json:
           return False
       else:
           return True
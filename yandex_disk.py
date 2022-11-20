import requests
from urllib.parse import quote

class YandexDisk:

   def __init__(self, access_token):
       self.token = access_token
       self.headers = {'Content-Type': 'application/json; charset=utf-8', 'Accept': 'application/json', 'Authorization': f'OAuth {access_token}'}
       self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

   def create_folder(self, path):
       """Создание папки. \n path: Путь к создаваемой папке."""
       requests.put(f'{self.url}?path={path}', headers=self.headers)

   def delete_folder(self, path):
       """Создание папки. \n path: Путь к создаваемой папке."""
       requests.delete(f'{self.url}?path={path}', headers=self.headers)

   def upload_file_by_url(self, load, savefile, replace=False):
       """Загрузка файла.
       savefile: Путь к файлу на Диске
       loadfile: Путь к загружаемому файлу
       replace: true or false Замена файла на Диске"""
       url = self.url + '/upload?path={0}'.format(quote(savefile)) + '&url={0}'.format(quote(load))
       requests.post(url, headers=self.headers).json()

   def check_folder(self, path):
       """Создание папки. \n path: Путь к создаваемой папке."""
       res = requests.get(f'{self.url}?path={path}', headers=self.headers).json()
       print(u'')
       if 'description' in res:
           if res['description'] == 'Resource not found.':
               response = True
           else:
               response = False
       else:
           response = False
       return response


#url = 'https://sun9-west.userapi.com/sun9-52/s/v1/ig2/tFp2VeZOpdXWElK10Qg-ykcZe-2CqGchf3upFF0pPtxyiR33O_6SXCYRllL9LZ9rSw3JTJxLEi_-N7NP8z5B2czU.jpg?size=500x500&quality=95&type=album'
#access_token = 'y0_AgAAAABeudekAAiihAAAAADUb3kRMddr5JnvQ7yFozZ2gKeps_WZqpY'
#yandex_disk = YandexDisk(access_token)
#yandex_disk.check_folder('today')
#yandex_disk.create_folder('hello')
#yandex_disk.upload_file_by_url(url, '2022-11-20/hello')
#yandex_disk.delete_folder('hello_world')
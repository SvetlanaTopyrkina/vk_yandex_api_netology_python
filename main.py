import json
from datetime import date

from vk import VK
from yandex_disk import YandexDisk

def save_photo(album, cnt = 5):
    i = 0
    f = open('log.txt', 'w', encoding='utf-8')
    for foto_name, foto_path in album.items():
        if i < cnt:
            name = str(today) + '/' + str(foto_name)
            yandex_disk.upload_file_by_url(foto_path, name)
            f.write(str(i) + '\n' + 'В алюбом ' + str(today) + ', загружена фотография ' + str(foto_name))
        else:
            pass
        i += 1
    f.close()

def save_json(js):
    with open('data.json', 'w') as outfile:
        json.dump(js, outfile)

if __name__ == '__main__':
    #Нам необходимо создать досутп к ВК
    access_token_vk = ''
    user_id = ''
    vk = VK(access_token_vk, user_id)
    #Нам необходимо подключиться к Yandex_disk
    access_token_yd = ''
    yandex_disk = YandexDisk(access_token_yd)
    #Теперь необходимо получить фотографии
    photos = vk.get_all_photos()
    #Теперь мы преобразуем фотографии в словарь вида {Название : url}
    album = vk.all_photos(photos)
    #Создавать папку будем на текущий_день, для этого проверим, а есть ли у нас уже такая папка
    today = date.today()
    #Проверим, а есть ли у нас папка
    i = 0
    while yandex_disk.check_folder(today) == False:
        today = str(today) + '_' + str(i)
        i += 1
    yandex_disk.create_folder(today)
    cnt = int(input("Введите количество фотографий для сохранения: "))
    save_photo(album, cnt)
    save_json(photos)
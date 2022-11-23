import json
from datetime import date

from vk import VK
from yandex_disk import YandexDisk

def save_photo(album, cnt = 5):
    i = 0
    f = open('log.txt', 'w', encoding='utf-8')
    if cnt > len(album):
        f.write('Введеное кол-во {0}'.format(cnt) + ' превышает, кол-во фотографий в альбоме {0}'.format(len(album)) + ' ,будет загружено на диск {0}'.format(len(album)) + ' фотографий.' +  '\n')
    for foto_name, foto_path in album.items():
        if i < cnt:
            name = str(today) + '/' + str(foto_name)
            if yandex_disk.upload_file_by_url(foto_path, name) == True:
                f.write(str(i) + '\n' + 'В алюбом ' + str(today) + ', загружена фотография ' + str(foto_name) + '\n')
            else:
                f.write(str(i) + '\n' + 'Не смог загрузить фотографию, по причине' + str(yandex_disk.upload_file_by_url(foto_path, name)) + '\n')
        else:
            pass
        i += 1
    f.close()

def save_json(js):
    with open('data.json', 'w') as outfile:
        json.dump(js, outfile)

if __name__ == '__main__':
    access_token_vk = ''
    user_id = ''
    vk = VK(access_token_vk, user_id)
    access_token_yd = ''
    yandex_disk = YandexDisk(access_token_yd)
    photos = vk.get_all_photos()
    if photos[0] == False:
        f = open('log.txt', 'w', encoding='utf-8')
        f.write(photos[1])
    else:
        album = vk.all_photos(photos[1])
        today = date.today()
        i = 0
        while yandex_disk.check_folder(today) == False:
            today = str(today) + '_' + str(i)
            i += 1
        if yandex_disk.create_folder(today) == True:
            cnt = int(input("Введите количество фотографий для сохранения: "))
            save_photo(album, cnt)
            save_json(photos)
        else:
            f = open('log.txt', 'w', encoding='utf-8')
            f.write(yandex_disk.create_folder(today))
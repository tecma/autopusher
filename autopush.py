#!/usr/bin/python3

import os, time, uuid # работа с ос, время, регулярки, создание уникальных строк
from subprocess import call # subprocess module (для прямой работы с sh)

EXEC_PATH = os.path.abspath(os.curdir)
FILES_PATH = EXEC_PATH+'/pusherfiles/'


def file_toucher(): # создаём случайные файлы

    file_id = (str(uuid.uuid4()).upper()[0:6]) # создаём уникальный id

    touch = open(FILES_PATH+file_id,"w") # создаём файл с этим ид
    touch.write(str(file_id)) # записываем в него id 
    touch.close()

    print('Создан случайный файл с ID: '+file_id)
    pass


def git_pusher():
    os.chdir(FILES_PATH)
    if (len(FILES_PATH) >= 5):
        call (['git', 'add', '*'])
        time.sleep(1)
        call (['git', 'commit', '-a', '--allow-empty-message', '-m', ' ', '-q' ])
        time.sleep(1)
        call (['git', 'push', '-q'])
        time.sleep(2.5)
    else:
        print ('Надо набрать 5 файлов')


def proc(file_count):

    file_count

    while True:
            time.sleep(1.2)
            file_toucher()
            file_count = file_count + 1
            # print (file_count)

            if file_count == 5:
                print('Создано ' + str(file_count) + ' случайных файла.')
                break  

proc(0)
git_pusher()


# if len(touch)


    # if file_count < 10:
    #     proc(0)
    # else:

    #     # remove('/home/tedudcaic/coding/projects/test_git_bot/pusher/*')   



# def git_pusher(timer):
#     call (['git', 'push'])
#     time.sleep(timer) # in seconds
#FILES
# a - открытие и добавление данных
# r - открытие для чтения данных
# w - открытие для записи данных
# w+, r+

#VARIANT 1
# colors = ['red','green','blue123'] 
# data = open('file.txt', 'a') # a- дозапись w- перезапись
# # data.writelines(colors) # разделителей нет
# data.write('\nLINE 12\n') # \n переоход перед записью
# data.write('LINE 13\n') # \n переход после записи
# data.close()

#VARIANT 2
# with open ('file.txt', 'a') as data:
#     data.write ('line 111111\n')
#     data.write ('line 33332\n')

#DATA READ
# path = 'file.txt'
# data = open(path, 'r') # r- режим чтения
# for line in data:# цикл бежит по файлу
#     print(line) # читаем строки
# data.close



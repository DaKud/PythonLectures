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


# FUNCTIONS AND MODULES

# import lec1 as h # чтобы не прописывать название полностью

# print(h.f(1))

# def new_string (symbol, count = 3):
#     return symbol * count
# print (new_string('!', 5)) # /!!!!!/
# print (new_string('!')) # TypeError missing 1 required...
# print (new_string(4)) # /12/, т.к произойдет умножение на 3, когда обявили count = 3

#Relative infinity - относительная бесконечность количества аргументов
 
# def concatenatio(*params): 
#     res: str = "" # логика как в работе со строкой, можно res: int = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a','s','d','w')) # /asdw/
# print(concatenatio('a','l','d','2')) # /ald2/
# print(concatenatio(1,2,3,4) # TypeError, а если res: int =0, то /10/ , числа  складываются

# FIBONACCI
# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib (n-2)
# list = []
# for e in range (1,10):
#     list.append(fib(e))
# print(list)# 1 1 2 3 5 8 13 21 34

# CORTEGE / Кортеж — упорядоченный набор фиксированной длины
# НЕИЗМЕНЯЕМЫЙ, НЕЛЬЗЯ СДЕЛАТЬ a[0]= 12 
# a = (3,4,5,45,566,0)
# print(a[-2])

# t = ()
# print (type(t)) #type

# t = (1,)
# print (type(t)) #type

# t = (1)
# print (type(t)) #int

# t = (28,9,1990)
# print (type(t)) #type

# colors = ['red','blue','green']
# print(colors)  #['red','blue','green']
# t = type(colors)
# print(t)

# t= tupe(['red','blue','green'])
# print(t[0]) #red
# print(t[2]) #blue
# print(t[10]) #IndexError ryple index out of range
# print(t[-2]) #green
# print(t[-200]) #IndexError ryple index out of range

# for e in t:
#     print(e) #red blue green

# Создвем список-> конвертируем в кортеж-> распаковываем кортеж в три независимые переменые
# t = type(['red','blue','green'])
# red, blue, green = t
# print('r: {} b:{} g:{}') #r:red b: blue g: green

# DICTIONARIES / СЛОВАРИ - НЕУПОРЯДОЧЕННЫЕ КОЛЛЕКЦИИ ПРОИЗВОЛЬНЫХ ОБЪЕКТОВ С ДОСТУПОМ ПО КЛЮЧУ

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑'
#         'right': '→'
#         'down': '↓'
#         'left': '←'
#     }
# # print(dictionary) # {'up' : '↑','right': '→','down' : '↓','left' : '←'}
# # print(dictionary['left']) # ←
# # типы ключей могут отличаться

# # ПОЛУЧИТЬ ВСЕ КЛЮЧИ
# for k in dictionary.keys():
#     print(k) # up right down left

# # ПОЛУЧИТЬ ВСЕ ЗНАЧЕНИЯ
# for k in dictionary.values():
#     print(k) # → ← ↓ ↑

#SET / МНОЖЕСТВА
# colors = {'red','blue','green'}
# print(colors) #{'red', 'blue', 'green'}
# colors.add ('grey') # ДОБАВЛЯЕМ {'blue', 'grey', 'green', 'red'}
# print(colors)
# colors.remove('red') # УДАЛЯЕМ {'green', 'grey', 'blue'}
# print(colors)
# colors.discard('red') # УДАЛЯЕМ {'green', 'grey', 'blue'}
# print(colors)
# colors.clear() # {}
# print(colors) #set()

#SET METHODS
a = {1,2,3,5,8}
b = {2,5,8,13,21}
c = a.copy() # c= {1,2,3,5,8} - МНОЖНСТВО НА ОСНОВЕ ИМЕЮЩЕГОСЯ
u = a.union(b) # u = {1,2,3,5,8,13,21} - ОБЪЕДИНЕНИЕ МНОЖНСТВ
i = a.intersection(b) #i = {8,2,5} - ПЕРЕСЕЧЕНИЕ
dl = a.difference(b) #dl = {1,3} - РАЗНОСТЬ
dr = b.difference(a) #dr = {13,21} - РАЗНОСТЬ

q = a \
    .union(b)\
    .difference(a.intersection(b))
#{1,21,3,13}

s = frozenset(a) # неизменяемый тип множества, никакие методы добавления /удаления НЕ работают


#FILES
# a - открытие и добавление данных
# r - открытие для чтения данных
# w - открыие для записи данных
# w+, r+

# A mode
colors = ['red','green','blue'] 
data = open('file.txt', 'a') # дозапись
data.writelies(colors) # разделителей нет
data.close()
#R mode

#W mode
# print('hello world')


# value = None # NONE- A VARIABLE, WHICH WE CAN DEFINE LATER
# print (type(value))

# from re import S


# a = 123
# b = 1.23
# s = 'hello world'
# s = "hello 'world" # OUTPUT WOULD LOOK LIKE /hello'world/
# print(type(a))
# print(type(b))
# value = 12345 # LOK UP AT NONE
# print (type(value)) # TO SHOW THE TYPE
# s = 'hello \nworld' # moving to another lvl string
# print(s) # PRINT THE STRING
# print (a,'-', b, '-', s)  # OUTPUT WOULD LOOK LIKE /123 - 1.23 - hello world/
# print ('{} - {} - {}'.format(a,b,s)) # formating print # OUTPUT WOULD LOOK LIKE /123 - 1.23 - hello world/
# print ('{1} - {2} - {0}'.format(a,b,s)) # changing places # OUTPUT WOULD LOOK LIKE /1.23 - hello world - 123/
# print (f'{a} - {b} - {s}') # interpolative print # OUTPUT WOULD LOOK LIKE /123 - 1.23 - hello world/

# f = True
# print (f) # OUTPUT WOULD LOOK LIKE /True/

# list = ['1', '2', '3', 'hello', 1, 2, 3, 4.5, True]
# print(list) #/['1','2',...]/

# DATA INPUT AND OUTPUT
# print, input

# print('Insert a')
# a = float (input())
# print('Insert b')
# b = float(input())
# print(a, '+' , b,'=', a+b)
# # print('{} {}'.format(a,b))
# # print(f'{a}  {b}')

# ARITHMETICAL OPERATIONS
# +,-,*,/,//(целочисленный результат деления),**(степень),%(остаток отделения))
# **, -number(отрицательное число),+number(положительное число),*,/,//,%,+,-
# a = 1.31231222222222222
# b = 3
# c = round(a*b, 5) # окугление
# print(c)

# (), Reduced operations

# a = 3
# a *= 5
# print(a)

# LOGICAL OPERATIONS
# >, >=, <=, ==, !=
# not, and, or - do not confuse with & ,| , ^
# Smth else : is, is not, in , not in

# f = [1,2,3,4]
# # print(f)
# # print(not 2 in f)

# is_odd = not f[0] % 2 #even or odd
# print(is_odd) 


# Control constructions
# if, if-else

# a = int(input('a = '))
# b = int(input('b ='))
# if a>b:
#     print(a)
# else:
#     print(b)




# username = input ('Insert name: ')
# if username == 'Maria':
#     print('MARIAAAAAAAAAAA')
# elif username == 'Herrero':
#     print('Herrero?')
# elif username == 'Krissy':
#     print('Krissy wake uuuup')
# else:
#     print('Hello', username)

# While
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print ('ok')
#     print ('enough')
# print(inverted)

#FOR
# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)


# r = range(10)
# for i in r:
#     print(i)

# for i in range (1,10,2): # от 1 до 10 с приращиванием на 2 ед
#     print(i)


# for i in 'qwe - rty':
#     print (i)




# text = 'съешь ещё этих мягких французских булок'

# help (text.istitle)
# print(len(text))          # 39
# print('ещё' in text)      # True
# print (text.isdigit())    # False
# print(text.islower())     # True
# print(text.replace('ещё', 'ЕЩЁ')) # 

# for c in text:
#     print(c)

# Lists
# numbers = [1,2,3,4,5]
# print(numbers)        # [1,2,3,4,5]
# ran= range (1, 6)
# numbers = list(ran)
# print(numbers)         # [1,2,3,4,5]
# numbers[0]= 10
# print(f'{len(numbers)} len')
# print(numbers)         # [10,2,3,4,5]
# for i in numbers:
#     i *= 2
#     print(i)           # [20,4,6,8,10]
# print(numbers)         # [10,2,3,4,5]


# colors = ['red','green','blue']
# for e in colors:
#     print(e)              # red,green,blue

# for e in colors:
#     print(e*2)            #redred #greengreen #blueblue

# colors.append('gray')     # put in the end
# print(colors == ['red','green','blue', 'gray']) # True
# colors.remove('red')   # del colors[0] # delete the element

# Functions
# def f(x):
#     if x == 1:
#         return ('Integer')
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 1
# print(f(arg))
# print(type(f(arg)))

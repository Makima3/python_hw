# strings
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'
st2 = ''
for i in st:
    if i.isdigit():
        st2 = ' ,'.join([st2, i])
print(st2)

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st_1 = 'as 23 fdfdg544 34'
print(','.join(''.join(elem if elem.isdigit() else ' ' for elem in st_1).split()))

# list comprehension
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
greeting = 'Hello, world'
print([alph.upper() for alph in greeting])
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
print([num**2 for num in range(50) if num % 2 != 0])

# function
# - створити функцію яка виводить ліст
def print_list(lst):
    for item in lst:
        print(item)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def f_num(a, b, c):
    num = max(a, b, c)
    print(num)
    return num

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def f_num2(*args):
    num1 = max(*args)
    num2 = min(*args)
    print(num1)
    return num2

# - створити функцію яка повертає найбільше число з ліста
list_func = [1,2,3,4,5,6,7,8,9]

def max_list(list_func):
    max1 = max(list_func)
    max_num = max1
    return max_num

# - створити функцію яка повертає найменьше число з ліста
def min_list(list_func):
    min1 = min(list_func)
    min_num = min1
    return min_num

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
list_func1 = [1,2,3,4,5,6,7,8,9]
def func_sum(list_func1):
    sum_num = sum(list_func1)
    return sum_num

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
average_list = [5, 8,6,12, 13, 14, 15, 16, 17, 18, 19]

def average(average_list):
    length_list = len(average_list)
    return sum(average_list) / length_list

# 1)Дан list:
list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
list1 = min(list)
print(list1)
#   - видалити усі дублікати
list2 = set(list)
print(list2)
#   - замінити кожне 4-те значення на 'X'
l1 = [22, 3,5,2,8,2,-23, 8,23,5]
for i in range(3, len(l1), 4):
    l1[i] = 'x'
print(l1)
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square (len_side):
    for i in range(len_side):
        if i == 0 or i == len_side - 1:
            print('*'* len_side)
        else:
            print('*' + ' ' * len_side + '*' )

square(6)

# 3) вывести табличку множення за допомогою цикла while

n = int(input('Enter a number: '))
i = 1
while i <= n:
    j = 1
    while j <= n:
        print('{:3}.'.format(i*j), end=' ')
        j += 1
    print()
    i += 1
# 4) переробити це завдання під меню

while True:
    print('1.  вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('2. знайти мін число')
    print('3. видалити усі дублікати')
    print('4. замінити кожне 4-те значення на X')
    print('5.  Exit')

    numb = input('Enter a number: ')

    if numb == '1':
        square(6)
    elif numb == '2':
        print(list1)
    elif numb == '3':
        print(list2)
    elif numb == '4':
        print(l1)
    elif numb == '5':
        print()
    break



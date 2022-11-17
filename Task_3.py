## Задайте список из нескольких чисел. Напишите программу, 
## которая найдёт сумму элементов списка, стоящих на нечётной позиции.

## Пример:
## - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


#########################################################################

# n = input('Введите размер списка: ')

# def is_int(k):
#     try:
#         int(k)
#     except:
#         print('Введено не корректное число.')
#         quit()

# is_int(n)
# n = int(n)
# new_list = []

# import random

# for i in range(n):
#     a = random.randint(0,30)
#     new_list.append(a)

# print(new_list)

# summ1 = 0
# for i in range(1,len(new_list),2):
#     summ1 += new_list[i]

# print(f'Сумма равна: {summ1}')


###########################################################################

from random import randint

n = input('Введите размер списка: ')

def is_int(k):
    try:
        int(k)
    except:
        print('Введено не корректное число.')
        quit()

is_int(n)
n = int(n)

new_list = [randint(0,30) for x in range(n)]
summ1 = sum(new_list[i] for i in range(n) if i%2==1)

print(new_list)
print(f'Сумма равна: {summ1}')

#######################################################################

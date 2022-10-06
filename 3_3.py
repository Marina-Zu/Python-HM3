# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

from random import sample

def ten_at_two (num):
    my_list = []
    while num > 0:
        my_list.append (num % 2)
        num = num // 2
    for i in range(-1, -(len(my_list)+1), -1):
        answer = my_list[i]
        print(answer, end = '')
    return answer

ten_at_two(int(input('Введите число > ')))
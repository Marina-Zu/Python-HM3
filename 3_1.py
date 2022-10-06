# Задайте список, состоящий из произвольных чисел, количество задает пользователь. 
# Напишите программу, которая найдет сумму элементов списка, 
# стоящих на нечетных позициях (не индексах)

from random import sample

def sum_odd_position (num):
    num = num if num > 0 else -num
    arr = sample(range(1, num* 2), num)
    print(arr)
    sum = 0
    for i in range (0, num, 2):
        sum += arr[i]
    return sum

print(sum_odd_position(int(input('Введите количество элементов списка > '))))
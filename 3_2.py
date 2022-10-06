# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def array (num):            # Функция заполнения списка
    num = num if num > 0 else -num
    arr = sample(range(-num, num* 2), num)
    print(arr)
    return arr

my_list = array ((int(input('Введите количество элементов списка > '))))

def sum_index_array (answer: list):
    my_list = []
    if len(answer) % 2 == 0:
        for i in range (len(answer)//2):
          my_list.append (answer[(i)] * answer[(len(answer)-1-i)])
    else:
        for i in range (len(answer)//2):
          my_list.append (answer[(i)] * answer[(len(answer)-1-i)])
        my_list.append (answer [len(answer)//2])
    print(my_list)
    return my_list
   
sum_index_array(my_list)
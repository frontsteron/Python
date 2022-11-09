# Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число. Напишите
# программу, которая определяет, есть в массиве
# последовательность из трёх элементов, совпадающая с
# введённым числом.

import random
def result():
    fifteen = [random.randint(100, 999) for i in range(15)] # Задан массив из случайных цифр от 100 до 999 на 15 элементов
    three = (input("Введите трёхзначное число - "))
    count = 0
    for i in range(0, len(fifteen) - 3): # условие
        if int(three[count]) == fifteen[i] and fifteen[i+1] == int(three[count+1]) and fifteen[i+2] == int(three[count+2]):
            return print(f"{fifteen} - {three} -> такое число в массиве есть")
            break
    return print(f"{fifteen} - {three} -> такого числа в массиве нет")
result()
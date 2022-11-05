﻿#Задача 1. Напишите программу, которая принимает на вход 
#число N и выдает список факториалов для чисел от 1 до N.
#N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Напши число N - '))
if n == -1 or n == 1:
    print(1)

elif n > 1:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(factorial)
    
elif n == 0:
    print('1')
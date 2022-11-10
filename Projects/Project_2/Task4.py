﻿# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.

print('Длинна списка - ')
length = int(input())
print('Элементы списка - ')
lst = list(map(int, input().split()))

move = 2

lst = lst[+move:] + lst[:+move]

print(lst)
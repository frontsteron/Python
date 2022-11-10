﻿# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

import math

# задаем кооридинаты 2ух точек
coordinate_A_x = float(input('Введите координату точки А по оси Х - '))
coordinate_A_y = float(input('Введите координату точки А по оси Y - '))
coordinate_B_x = float(input('Введите координату точки B по оси Х - '))
coordinate_B_y = float(input('Введите координату точки B по оси Y - '))

# расстояние между двумя точками, с координатами X и Y
distance = round(math.sqrt((coordinate_B_x - coordinate_A_x)**2 + (coordinate_B_y - coordinate_A_y)**2), 2)
print(distance)
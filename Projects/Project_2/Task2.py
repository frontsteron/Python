﻿# Задача 2. Выведите таблицу истинности для 
# выражения ¬(X ∧ Y) ∨ Z.

print('x', 'y', 'z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, bool(not (x and y) or z))
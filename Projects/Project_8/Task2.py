# Дана квадратная матрица, заполненная случайными числами. Определите,
# сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random

rows = columns = 5 # размер матрицы
sumDiagonal = 0
sumEl = 0
numbers = [0] * rows 
line = 1

for i in range(len(numbers)):
    numbers[i] = list(0 for _ in range(columns))

for i in range(rows):
    for j in range(columns):
        current_number = random.randint(0, 50)
        numbers[i][j] = random.randint(0, 50)
        if i == j:
            sumDiagonal += numbers[i][j]
        
print("\nKвадратная матрица, заполненная случайными числами:")
for row in numbers:
    print(row)

print(f'\nСуммa главной диагонали - {sumDiagonal}')  

for i in range(rows):
    for j in range(columns):
        sumEl += numbers[i][j]
    if sumEl > sumDiagonal:
        print(f'Сумма элементов {line} строки {sumEl}, превосходит сумму главной диагонали матрицы.')
    sumEl = 0
    line += 1
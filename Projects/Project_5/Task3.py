﻿# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.

from random import randrange as rr

def getNumber(*args): return int(input(*args))

def createRange(n, minValue=1, maxValue=10): return [rr(minValue, maxValue + 1) for _ in range(n)]

def filterElements(numbers:list): return list(filter(lambda x: numbers.count(x) == 1, numbers))

def main():
    length = getNumber('Укажи желаемую длину списка - ')
    numbers = createRange(length)
    print('Список случайных элементов - ', *numbers)
    nonRepeatNumbers = filterElements(numbers)
    print('Список с уникальными значениями - ', *nonRepeatNumbers)
    print(f'Количество повторяющихся элементов - {(len(numbers)-len(nonRepeatNumbers))*2}')

if __name__ == '__main__':
    main()
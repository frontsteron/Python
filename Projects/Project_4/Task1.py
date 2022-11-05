﻿# Задача 1. Задайте натуральное число N. Напишите
# программу, которая составит список простых множителей
# числа N.

import math
print('Введи натуральное число и я составлю список простых его множителй - ')
def getIntNumber(): return int(input())

def checkPrime(n: int, multipliers: list):
    if n % 2 == 0:
        multipliers.append(2)
        return n // 2
    if n % 3 == 0:
        multipliers.append(3)
        return n // 3
    for i in range(1, math.ceil(n ** 0.5) + 1):
        if n % (6 * i - 1) == 0:
            multipliers.append(6 * i - 1)
            return n // (6 * 1 - 1)
        if n % (6 * i + 1) == 0:
            multipliers.append(6 * i + 1)
            return n // (6 * i + 1)

def findmultipliers(number: int):
    multipliers = []
    while number != 1:
        number = checkPrime(number, multipliers)
    return multipliers

def main():
    n = getIntNumber()
    multipliers = findmultipliers(n)
    print(f'Простые множители {n} это -',*multipliers)

if __name__ == '__main__':
    main()
# Задайте список случайных чисел от 1 до 10, 
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.

from random import randrange as rr

def getLenArr(*args): return int(input(*args)) #вводим желаемую длину

def createRange(n, minValue=1, maxValue=10): return [rr(minValue, maxValue + 1) for _ in range(n)] #делаем диапозон

def filterNum(numbers): return filter(lambda x: x > 5, numbers) #фильтруем диапазон с лямбдой

def main():
    length = getLenArr('Укажи желаемую длину списка - ') #задаем длинну массива
    numbers = createRange(length) #
    print('Случайные числа от 1 до 10 - ', *numbers)
    print('Элементы при условии больше 5 - ', *filterNum(numbers))

if __name__ == '__main__':
    main()
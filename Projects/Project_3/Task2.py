# В файле находятся названия фруктов.
# Выведите все фрукты, названия которых начинаются на
# заданную букву.

def getFirstLetter(): return input()[0]
print('Введи первую букву фрукта и я тебе покажу фрукты на эту букву - ')

def findFruits(letter:str):
    with open('fruits.txt', 'r', encoding='utf-8') as inf:
        fruits = [inf.readline().strip().replace('\n','') for _ in inf]
    print(fruits)
    for fruit in fruits:
        if fruit and fruit[0].lower() == letter.lower():
            print(fruit)

def main():
    char = getFirstLetter()
    findFruits(char)

if __name__ == '__main__':
    main()
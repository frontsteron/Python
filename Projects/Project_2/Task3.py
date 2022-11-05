# Даны две строки. Посчитайте сколько раз
# каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

print('Введи первую строку - ')
line1 = input()
print('Введи вторую строку - ')
line2 = input()

for symbol in set(line1):
    print(symbol,': ',line2.count(symbol))
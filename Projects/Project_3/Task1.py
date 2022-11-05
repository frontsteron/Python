# Создайте файл. Запишите в него N первых
# элементов последовательности Фибоначчи.

print('Введи сколько записать в файл первых элементов последовательности Фибоначчи - ')

def fibCreat(n):
    f1, f2 = 1, 1
    with open('figure.txt', 'w', encoding='utf-8') as ouf:
        ouf.write(f'Последовательность Фибоначчи - {n} \n')
        for i in range(1, n + 1):
            ouf.write(str(i) + ':\t' + str(f1) + '\n')
            f1, f2 = f2, f1 + f2

def main():
    n = int(input())
    fibCreat(n)

if __name__ == '__main__':
    main()
# Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000
# рублей.
# Предоставьте ему графические данные о стоимость квадратного метра каждого дома и
# список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров,
# цены от 3 до 20 млн.

from matplotlib import pyplot as plt  
import random

areaHouses = [random.randint(100, 300) for i in range(0, 15)]
priceHouses = [random.randint(3000000, 20000000) for i in range(0, 15)]

x = []
squareMeter = []
lowPrise = []
sortedHouses = []

for i in range(0, 15):
    x.append(i+1)

for i in range(len(areaHouses)):
    squareMeter.append(round(priceHouses[i]/areaHouses[i]))

for i in range(len(squareMeter)):
    if squareMeter[i] < 50000:
        lowPrise.append(squareMeter[i])
        sortedHouses.append(areaHouses[i])

for i in range(len(sortedHouses)-1):
    for j in range(len(sortedHouses)-i-1):
        if sortedHouses[j] > sortedHouses[j+1]:
            lowPrise[j], lowPrise[j+1] = lowPrise[j+1], lowPrise[j]
            sortedHouses[j], sortedHouses[j+1] = sortedHouses[j+1], sortedHouses[j]

print('\nДома стоимость квадратного метра которых меньше 50000 рублей, это:')
for i in range(len(lowPrise)):
    print(f'Дом №{i+1} с площадью {sortedHouses[i]} кв.м., при стоимости {lowPrise[i]} за кв.м')

plt.title('Рыночная стоимости кв.м. дома')
plt.xlabel('Номер дома')    
plt.ylabel('Стоимость кв.м.')  
plt.grid(which='major')

plot2 = list(50000 for a in range(1, 16))
plt.plot(x, plot2)
plt.plot(x, squareMeter, 'yo')
plt.show()
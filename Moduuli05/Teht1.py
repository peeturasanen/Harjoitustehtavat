import random

kuutiot = int(input('Anna arpakuutioiden lukumäärä: '))
summa = 0
i = 0
for i in range(kuutiot):
    summa = summa + random.randint(1,6)
print(summa)
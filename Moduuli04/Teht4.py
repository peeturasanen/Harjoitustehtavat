import random

arvaus = int(input('Anna luku 1-10: '))
arvo = random.randint(1,10)
while arvaus!=arvo:
    if arvaus > arvo:
        print('Liian suuri arvaus.')
    elif arvaus < arvo:
        print('Liian pieni arvaus.')
    arvaus = int(input('Anna luku 1-10: '))
print('Oikein!')
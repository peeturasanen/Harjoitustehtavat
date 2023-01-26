import random
tahkot = int(input('Anna nopan tahkojen määrä: '))
def arvo(määrä):
    luku = random.randint(1, määrä)
    return luku
noppa = 0
while noppa < tahkot:
    noppa = arvo(tahkot)
    print(noppa)
    if noppa == tahkot:
        print('Toiminto lopetettu.')
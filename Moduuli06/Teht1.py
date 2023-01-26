import random
def arvo():
    luku = random.randint(1,6)
    return luku
noppa = 0
while noppa < 6:
    noppa = arvo()
    print(noppa)
    if noppa == 6:
        break

print('Toiminto lopetettu.')
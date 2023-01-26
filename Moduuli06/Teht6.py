import math
def pizza(halkaisija, hinta):
    sade = halkaisija/2
    alacm2 = math.pi * sade**2
    euroa = hinta / alacm2
    ykshinta = euroa * 10000
    return ykshinta

halkaisija1 = float(input('Anna ensimmäisen pizzan halkaisija senttimetreinä: '))
hinta1 = float(input('Anna ensimmäisen pizzan hinta: '))
halkaisija2 = float(input('Anna toisen pizzan halkaisija senttimetreinä: '))
hinta2 = float(input('Anna toisen pizzan hinta: '))

if pizza(halkaisija1,hinta1) > pizza(halkaisija2,hinta2):
    print('Toisen pizzan yksikkö hinta on pienempi.')
else: print('Ensimmäisen pizzan yksikkö hinta on pienempi.')
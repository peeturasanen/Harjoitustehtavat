vuosiluku = int(input('Anna vuosiluku: '))
if vuosiluku % 100 == 0:
    if vuosiluku % 400 == 0:
        print('Vuosi on karkausvuosi.')
    else:
        print('Vuosi ei ole karkausvuosi.')
elif vuosiluku % 4 == 0:
    print('Vuosi on karkausvuosi.')
else:
    print('Vuosi ei ole karkausvuosi.')
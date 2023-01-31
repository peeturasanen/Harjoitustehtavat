nimet = set()
nimi = ' '
while nimi != '':
    nimi = input('Anna nimi: ')
    if nimet.__contains__(nimi):
        print('Aiemmin syötetty nimi')
        nimet.add(nimi)
    else:
        print('uusi nimi')
        nimet.add(nimi)

for n in nimet:
    print(n)
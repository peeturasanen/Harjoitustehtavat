tunnus = input('Anna käyttäjätunnus: ')
salasana = input('Anna salasana: ')
x = 1
while (tunnus!='python' or salasana!='rules'):
    if x >= 5:
        print('Pääsy evätty!')
        break
    print('Väärä käyttäjätunnus tai salasana.')
    print()
    tunnus = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')
    x = x + 1

else:
    print('Tervetuloa!')
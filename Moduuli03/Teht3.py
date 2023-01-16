suku = input('Anna biologinen sukupuoli(nainen/mies): ')
hemo = int(input('Anna hemoglobiiniarvo(g/l): '))
if suku == 'nainen':
    if hemo <= 116:
        print('Hemoglobiini arvosi on alhainen')
    elif hemo >= 176:
        print('Hemoglobiiniarvosi on korkea')
    else:
        print('Hemoglobiiniarvosi on normaali.')
if suku == 'mies':
    if hemo <= 133:
        print('Hemoglobiiniarvosi on alhainen.')
    elif hemo >= 196:
        print('Hemoglobiiniarvosi on korkea.')
    else:
        print('Hemoglobiiniarvosi on normaali.')
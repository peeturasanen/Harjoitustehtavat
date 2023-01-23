lista = []
luku = input('Anna luku: ')
while luku!='':
    lista.append(int(luku))
    luku = input('Anna toinen luku: ')
    lista.sort(reverse=True)
print(lista[0:5])
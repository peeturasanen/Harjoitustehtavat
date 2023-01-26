def summa(lista):
    tulos = 0
    for n in range(len(lista)):
        tulos = tulos + lista[n]
    return tulos
lista1 = [1, 2, 3, 4, 5, 6]
print('Listan summa on:')
print(summa(lista1))
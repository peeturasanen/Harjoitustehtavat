def f(lista):
    lista2 =[]
    print(lista)
    for n in range(len(lista)):
        if lista[n] % 2 == 0:
            lista2.append(lista[n])
    return print(lista2)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8,]

f(lista1)
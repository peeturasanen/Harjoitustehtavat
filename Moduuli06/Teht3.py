gallonat = float(input('Anna gallona määrä: '))
def litrat(määrä):
    litrat = määrä * 3.785
    return litrat

while gallonat >= 0:
    print(litrat(gallonat))
    print('Litraa')
    gallonat = float(input('Anna gallona määrä: '))
    if gallonat < 0:
        print('Ei voi muuntaa, toiminto lopetettu.')
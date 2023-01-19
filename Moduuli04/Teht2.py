tuuma = int(input('Anna tuumien määrä: '))
while tuuma >= 1:
    if (tuuma < 1):
        break
    print('Senttimetreinä: ' + str(tuuma * 2.54))
    tuuma = int(input('Anna tuumien määrä: '))
print('Toiminto lopetettu.')
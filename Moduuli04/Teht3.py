max = -9999999999999999999999999999999999999999999999999999999999999999999999999999999
min = 9999999999999999999999999999999999999999999999999999999999999999999999999999999

while True:
    luku = (input('Anna luku: '))
    if luku == '':
        break
    if int(luku) > max:
        max = int(luku)
    if int(luku) < min:
        min = int(luku)

print('Suurin luku: ' + str(max))
print('Pienin luku: ' + str(min))
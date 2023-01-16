leiviskat = float(input('Anna leiviskät: '))
naulat = float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

luoti = 13.3
naula = 32 * luoti
leiviska = 20 * naula

luotig = luodit * luoti
naulag = naulat * naula
leiviskag = leiviskat * leiviska

grammatg = luotig + naulag + leiviskag

kilot = (int(grammatg / 1000))
grammat = (float(grammatg % 1000))

print('Massa nykymittojen mukaan: ')
print(kilot + 'kiloa ja ' + grammat + ' grammaa.')
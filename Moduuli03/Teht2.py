hyttilk = str(input('Anna hyttiluokka(LUX, A, B, C): '))
if hyttilk == 'LUX':
    print('LUX on parvekkeellinen hytti autokannen yläpuolella.')
elif hyttilk == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hyttilk == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hyttilk == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka.')

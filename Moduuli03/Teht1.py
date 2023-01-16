kuhacm = float(input('Annan kuhan pituus(cm): '))
alamitta = 37 - kuhacm
if kuhacm <= 36:
    print('Kuha on ' + str(alamitta) + 'cm alamittainen, laske se takaisin järveen.')
else:
    print('Kuha on täysimittainen.')
asemat = {}
toiminto = input('Haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa? Syötä (uusi), (haku) tai (lopeta): ')
while toiminto != 'lopeta':
    if toiminto == 'uusi':
        nimi = input('Anna lentokentän nimi: ')
        koodi = input('Anna lentokentän ICAO-koodi: ')
        asemat[koodi] = nimi
    elif toiminto == 'haku':
        haku = input('Anna lentokentän ICAO-koodi: ')
        if haku in asemat:
            print('Koodi vastaa lentoasemaa: ' + asemat[haku])
    toiminto = input('Haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa? Syötä (uusi), (haku) tai (lopeta): ')
import mysql.connector
def lentokentta(ICAO):
    sql = 'SELECT name, municipality from airport'
    sql += " WHERE ident='" + ICAO + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >= 0:
        for rivi in tulos:
            print(f'Lentokenttä: {rivi[0]}. Kunta on {rivi[1]}')
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='spietu',
         password='python',
         autocommit=True)

ICAO = input('Anna ICAO-Koodi: ')
lentokentta(ICAO)
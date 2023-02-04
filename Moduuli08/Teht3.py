import mysql.connector
from geopy.distance import geodesic
def lentokentta(ICAO):
    sql = 'SELECT latitude_deg, longitude_deg from airport'
    sql += " WHERE ident='" + ICAO + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >= 0:
        for rivi in tulos:
            asema = (rivi[0], rivi[1])
    return asema

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='spietu',
         password='python',
         autocommit=True)

ICAO1 = input('Anna ICAO-Koodi: ')
ICAO2 = input('Anna toinen ICAO-Koodi: ')
print('Lentokenttien välinen etäisyys on: ' + str(geodesic(lentokentta(ICAO1), lentokentta(ICAO2)).km.__round__(1)) + 'km')
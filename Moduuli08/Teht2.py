import mysql.connector
def lentokentat(maakoodi):
    sql = 'SELECT type from airport'
    sql += " WHERE iso_country='" + maakoodi + "'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    luku = {i: tulos.count(i) for i in tulos}
    print(luku)
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='spietu',
         password='python',
         autocommit=True)

maakoodi = input('Anna maakoodi: ')
lentokentat(maakoodi)
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def lentokentta(icao):
    sql = 'SELECT name, municipality from airport'
    sql += " WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='spietu',
         password='python',
         autocommit=True)


@app.route('/kenttä/<icao>')
def info(icao):
    airport_info = lentokentta(icao)
    cc = {
        "ICAO": icao,
        "Name": airport_info[0][0],
        "Municipality": airport_info[0][1]
    }
    return jsonify(cc)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

# http://127.0.0.1:3000/kenttä/EFHK

from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def alkuluku1(luku):
    if luku == 1:
        return False
    elif luku > 1:
        for n in range(2, luku):
            if (luku % n) == 0:
                return False
        else:
            return True
    else:
        return False


@app.route('/alkuluku/<int:luku>')
def alkuluku2(luku):
    cc = {"Number": luku, "isPrime": alkuluku1(luku)}
    return jsonify(cc)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

# http://127.0.0.1:3000/alkuluku/31

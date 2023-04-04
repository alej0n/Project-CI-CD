"""from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def bienvenido():
    return jsonify({'message': 'Bienvenido'})
    



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)    """

from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        result = int(a) + int(b)
        return str(result)
    else:
        a = request.args.get('a')
        b = request.args.get('b')
        result = int(a) + int(b)
        return str(result)

@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        result = int(a) - int(b)
        return str(result)
    else:
        a = request.args.get('a')
        b = request.args.get('b')
        result = int(a) - int(b)
        return str(result)

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        result = int(a) * int(b)
        return str(result)
    else:
        a = request.args.get('a')
        b = request.args.get('b')
        result = int(a) * int(b)
        return str(result)

@app.route('/divide', methods=['GET', 'POST'])
def divide():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        result = int(a) / int(b)
        return str(result)
    else:
        a = request.args.get('a')
        b = request.args.get('b')
        result = int(a) / int(b)
        return str(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

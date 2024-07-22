from flask import Flask, jsonify

#
app = Flask(__name__)

dados = {'nome': 'Samuel', 'idade': 22, 'municipio': 'São José dos Campos'}
@app.route('/')
def index():
    return jsonify(dados)




if __name__ == '__main__':
    app.run(debug=True)
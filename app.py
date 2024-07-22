from flask import Flask, jsonify
from flask_cors import CORS

#
app = Flask(__name__)

#Definindo cors
CORS(app, origins=['http://localhost:5173/'])

dados = {'nome': 'Samuel', 'idade': 22, 'municipio': 'São José dos Campos'}
@app.route('/')
def index():
    return jsonify(dados)




if __name__ == '__main__':
    app.run(debug=True)
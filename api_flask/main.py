from flask import Flask, request
from flask import json
from flask.json import jsonify

from src.SaveData import add_data, get_best_clients

app = Flask(__name__)

@app.route('/')
def ping():
    return jsonify({"Message": "Probando servidor"})

@app.route('/new_data', methods=['POST'])
def new_data():     
    #Solicitando datos    
    data = request.data
    add_data(data)
    return jsonify({"Message": "Probando, probando"})

@app.route('/best_clients', methods=['GET'])
def best_clients():
    return get_best_clients()


if __name__ == "__main__":
    app.run(debug=True, port=4000)
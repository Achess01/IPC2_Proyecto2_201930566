from flask import Flask, request
from flask import json
from flask.json import jsonify

from src.SaveData import *

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

@app.route('/most_selled')
def most_selled():
    return get_best_games()

@app.route('/games_classification')
def games_classification():
    return get_games_classification()

@app.route('/birthdays')
def birhdays():
    return get_birthdays()
    
@app.route('/games')
def games():
    return get_games()

if __name__ == "__main__":
    app.run(debug=True, port=4000)
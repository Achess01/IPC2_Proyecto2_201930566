from flask import Flask, request
from flask import json
import flask
from flask.helpers import make_response
from flask.json import jsonify

from src.SaveData import *

app = Flask(__name__)

@app.route('/')
def ping():
    return jsonify({"Message": "Probando servidor"})

@app.route('/new_data', methods=['POST'])
def new_data():     
    #Solicitando datos    
    try:
        data = request.data        
        print(data)
        add_data(data)
        response = jsonify({"Message": "Datos agregados"})
        return response
    except ValueError:         
        # return jsonify({"Message": "Error al guardar los datos"})
        response = jsonify({"Message": "Datos no agregados"})
        return response

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
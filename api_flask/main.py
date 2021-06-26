from flask import Flask, request
from flask import json
from flask.json import jsonify

from src.SaveData import add_data

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


if __name__ == "__main__":
    app.run(debug=True, port=4000)
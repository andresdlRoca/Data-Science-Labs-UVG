from keras.models import load_model
import numpy as np
import joblib
from flask import Flask, request, jsonify

modelo = load_model('modelo.h5')

def getPricePrediction(city, area, rooms, bathroom, parking_spaces, floor, animal, furniture):
    return "testing"

app = Flask(__name__)
@app.route('/modelo', methods=['GET'])
def getPrice(): # Obtener precio de alquiler total
    price_prediction = getPricePrediction(request.args.get('city'), request.args.get('area'), request.args.get('rooms'), request.args.get('bathroom'), request.args.get('parking_spaces'), request.args.get('floor'), request.args.get('animal'), request.args.get('furniture'))
    return jsonify(price_prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

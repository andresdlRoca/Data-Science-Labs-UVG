from keras.models import load_model
import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, jsonify


# input_data = {
#     'city': ['São Paulo', 'Campinas'],
#     'rooms': [2, 2],
#     'bathroom': [1, 1],
#     'parking_spaces': [1, 1],
#     'fire_insurance_(r$)': [17, 17],
#     'furniture': ['furnished', 'furnished']
# }

# input_df = pd.DataFrame(input_data)


# predictions = model.predict(input_df)

# print(predictions)

model = joblib.load('../modelo.joblib')

def getPricePrediction(city, rooms, bathroom, parking_spaces, fire_insurance, furniture):
    input_data = {
        'city': [city],
        'rooms': [rooms],
        'bathroom': [bathroom],
        'parking_spaces': [parking_spaces],
        'fire_insurance_(r$)': [fire_insurance],
        'furniture': [furniture]
    }

    input_df = pd.DataFrame(input_data)

    predictions = model.predict(input_df)

    return predictions[0]

app = Flask(__name__)
@app.route('/modelo', methods=['GET'])
def getPrice():
    price_prediction = getPricePrediction(request.args.get('city'), request.args.get('rooms'), request.args.get('bathroom'), request.args.get('parking_spaces'), request.args.get('fire_insurance'), request.args.get('furniture'))
    return str(price_prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

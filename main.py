from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained prediction model
model = pickle.load(open('car_price_prediction_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('pages/index.html')

@app.route('/predict', methods=['POST'])
def predict():
    prix_vente = float(request.form['price_vente'])
    kilometrage = float(request.form['kilometrage'])
    puissance = int(request.form['puissance'])
    prix_achat = float(request.form['price_achat'])
    age = int(request.form['age'])
    marque = request.form['marque']

    # Encoding marque
    marque_Peugeot = 0
    marque_Renault = 0
    marque_Toyota = 0
    marque_Volkswagen = 0

    if marque == 'Peugeot':
        marque_Peugeot = 1
    elif marque == 'Renault':
        marque_Renault = 1
    elif marque == 'Toyota':
        marque_Toyota = 1
    elif marque == 'Volkswagen':
        marque_Volkswagen = 1

    carburant = request.form['carburant']
    carburant_Essence = 0
    if carburant == 'Essence':
        carburant_Essence = 1

    # Prepare variables for prediction
    prediction = model.predict([[kilometrage, puissance, prix_achat, age, marque_Peugeot, marque_Renault, marque_Toyota, marque_Volkswagen, carburant_Essence]])

    # Perform the prediction
    output = round(prediction[0], 2)
    if output < 0:
        return render_template('pages/index.html', prediction_texts="Sorry you cannot sell this car")
    else:
        return render_template('pages/index.html', prediction_text="You Can Sell The Car at {}".format(output))


if __name__ == '__main__':
    app.run(debug=True)





if __name__ == '__main__':
    app.run(debug=True)

# Importing the required libraries
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from joblib import load
import pandas as pd
import datetime

# Setting up our Flask app
app = Flask(__name__)

# Making sure our app can handle requests from different origins
CORS(app)

# Loading our trained model and encoder for later use
regression_model = load('model.joblib')
encoder = load('encoder.joblib')

@app.route('/')
def serve_homepage():
    # When users visit the main page, show them the homepage template
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'OPTIONS'])
@cross_origin()
def make_prediction():
    # This function handles the prediction process
    
    # Grabbing the data sent by the user
    data = request.json
    df_input = pd.DataFrame(data)

    # Transforming certain features so our model can understand them
    encoded_features = encoder.transform(df_input[['brand', 'fuel', 'gearbox']]).toarray()
    df_encoded_features = pd.DataFrame(encoded_features)

    # Figuring out how old the car is based on its year
    current_year = datetime.datetime.now().year
    df_input['age'] = current_year - df_input['year']

    # Merging our transformed features with the other features
    df_numerical_input = df_input[['age', 'mileage (kms)']]
    df_final_input = pd.concat([df_numerical_input, df_encoded_features], axis=1)
    df_final_input.columns = df_final_input.columns.astype(str)

    # Asking our model for a price prediction
    predicted_price = regression_model.predict(df_final_input)
    
    # Sending the prediction back to the user
    return jsonify({"predicted_price": f"€{predicted_price[0]:.2f}"})

# If this script is run directly, start up the Flask app
if __name__ == '__main__':
    app.run(debug=True)

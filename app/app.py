"""Flask API that creates POST requests to the prediction model and get a predicted car value"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from joblib import load
import pandas as pd
import datetime

app = Flask(__name__)
CORS(app)

# Load the regression model and encoder
regression_model = load('model.joblib')
encoder = load('encoder.joblib')

@app.route('/')
def serve_homepage():
    """Serve the main homepage."""
    return render_template('index.html')
@app.route('/predict', methods=['POST', 'OPTIONS'])
@cross_origin()
def make_prediction():
    """Make a prediction based on the provided data."""
    data = request.json
    df_input = pd.DataFrame(data)

    # One-hot encode categorical features
    encoded_features = encoder.transform(df_input[['brand', 'fuel', 'gearbox']]).toarray()
    df_encoded_features = pd.DataFrame(encoded_features)

    # Calculate age from the year
    current_year = datetime.datetime.now().year
    df_input['age'] = current_year - df_input['year']

    # Combine numerical and encoded features
    df_numerical_input = df_input[['age', 'mileage (kms)']]
    df_final_input = pd.concat([df_numerical_input, df_encoded_features], axis=1)
    df_final_input.columns = df_final_input.columns.astype(str)

    # Make the prediction
    predicted_price = regression_model.predict(df_final_input)
    return jsonify({"predicted_price": f"€{predicted_price[0]:.2f}"})

if __name__ == '__main__':
    app.run(debug=True)
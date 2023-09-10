"""Flask API that allows a user to call it and get a predicted car value"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_homepage():
    """Serve the main homepage."""
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'OPTIONS'])
@cross_origin()
def make_prediction():
    """
    Make a prediction based on the provided data.
    Note: Need to add actual prediction logic
    """
    data = request.json
    # Placeholder for prediction logic
    predicted_price = 0
    return jsonify({"predicted_price": f"€{predicted_price:.2f}"})

if __name__ == '__main__':
    app.run(debug=True)
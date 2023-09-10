"""Flask API that allows a user to call it and get a predicted car value"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main homepage."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
"""
A Flask endpoint to access the model and make predictions with it
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
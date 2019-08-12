from flask import Flask, request, jsonify

from model import load_model

app = Flask(__name__)
model = load_model()


@app.route('/')
def index():
    return f'Serving a {model.__class__.__name__} model using Flask.'


@app.route('/predict', methods=['POST'])
def predict():
    body = request.get_json(force=True)
    prediction = model.predict(body['X'])
    return jsonify({'y': prediction.tolist()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')

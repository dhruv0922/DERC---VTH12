from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the pre-trained model
model = load_model('saved_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get data from POST request
    features = np.array([data['feature1'], data['feature2'], data['feature3']])  # Customize this
    prediction = model.predict(features.reshape(1, -1))
    return jsonify({'predicted_price': prediction[0][0]})

if __name__ == "__main__":
    app.run(debug=True)

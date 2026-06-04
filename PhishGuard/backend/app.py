from model.feature_extract import extract_features
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load(
    r"E:\Data\PhishGuard\backend\model\phishguard_model.pkl"
)

@app.route("/")
def home():
    return "PhishGuard is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    url = data["url"]

    features = extract_features(url)

    prediction = model.predict([features])[0]

    print("Features =", features)
    print("Prediction:", prediction)

    if prediction == 1:
        result = "SAFE WEBSITE ✅"
    else:
        result = "PHISHING WEBSITE 🚨"

    return jsonify({
            "prediction": result
        })
    
if __name__ == "__main__":
    app.run(debug=True)
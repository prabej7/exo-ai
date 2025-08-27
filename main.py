from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load("final_model_90.joblib")


@app.route("/", methods=["GET"])
def index():
    return {"message": "Welcome to API!"}


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = data.get("features")
    if features is None:
        return jsonify({"error": "No features provided"}), 400

    try:
        # ensure it's shaped correctly for sklearn
        prediction = model.predict([features])
        classes = {0: "FALSE POSITIVE", 1: "CONFIRMED", 2: "CANDIDATE"}
        return jsonify({"prediction": classes[int(prediction[0])]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

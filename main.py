from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the model
try:
    model = joblib.load("final_model_90.joblib")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


@app.route("/", methods=["GET"])
def index():
    return {"message": "Welcome to NASA Space App Challenge API!", "status": "healthy"}


@app.route("/health", methods=["GET"])
def health():
    model_status = "healthy" if model is not None else "unhealthy"
    return {
        "status": "healthy",
        "model_status": model_status,
        "timestamp": "2025-01-27T00:00:00Z",
    }


@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not available"}), 503

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

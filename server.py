from flask import Flask, request, jsonify
from emotion_detection import emotion_detector
import subprocess

app = Flask(__name__)


@app.route("/emotion", methods=["POST"])
def emotion_api():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Bad Request"}), 400

    result = emotion_detector(data["text"])
    return jsonify(result), 200


@app.route("/", methods=["GET"])
def home():
    return {"status": "Emotion API Running"}, 200


# =========================
# TASK 8: Static Analysis
# =========================
def run_static_analysis():
    result = subprocess.run(
        ["flake8", "."],
        capture_output=True,
        text=True
    )

    print("STATIC ANALYSIS OUTPUT:")
    print(result.stdout if result.stdout else "No issues found (Perfect Score)")


if __name__ == "__main__":
    run_static_analysis()
    app.run(host="0.0.0.0", port=5000, debug=True)
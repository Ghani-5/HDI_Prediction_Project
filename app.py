from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoder
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    life = float(request.form["life"])
    expected = float(request.form["expected"])
    mean = float(request.form["mean"])
    gni = float(request.form["gni"])

    data = np.array([[life, expected, mean, gni]])

    prediction = model.predict(data)

    result = encoder.inverse_transform(prediction)[0]

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)
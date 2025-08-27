from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load saved model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        age = float(request.form['age'])
        sex_male = float(request.form['sex_male'])
        cigsPerDay = float(request.form['cigsPerDay'])
        totChol = float(request.form['totChol'])
        sysBP = float(request.form['sysBP'])
        glucose = float(request.form['glucose'])

        # Prepare input
        input_features = np.array([[age, sex_male, cigsPerDay, totChol, sysBP, glucose]])

        # Scale input using saved scaler
        input_scaled = scaler.transform(input_features)

        # Predict class (0/1)
        prediction = model.predict(input_scaled)

        # Predict probability
        probability = model.predict_proba(input_scaled)[0][1]  # probability of class 1
        probability_percent = round(probability * 100, 2)

        if prediction[0] == 1:
            result = f"Heart Disease Risk: YES ({probability_percent}%)"
        else:
            result = f"Heart Disease Risk: NO ({probability_percent}%)"

        return render_template('index.html', prediction_text=result)
    
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

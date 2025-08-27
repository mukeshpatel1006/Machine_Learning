Prepare your project folder
Make sure your folder structure looks like this:
Heart_Disease_Prediction/
│
├── app.py # Flask app
├── train_model.py # Script to train and save the model
├── model.pkl # Saved trained model
├── scaler.pkl # Saved scaler
├── requirements.txt # Required Python packages
└── templates/
└── index.html # HTML template for frontend

## Dependencies

Install dependencies using:

```bash
pip install -r requirements.txt

Required packages:
Flask
scikit-learn
pandas
numpy
matplotlib
seaborn

Step 1: Train the Model
Run the training script to generate the model and scaler:
python train_model.py
This creates model.pkl and scaler.pkl which are used by the Flask app
Step 2: Run the Flask App
python app.py
The app will start at http://127.0.0.1:5000/.
Open this URL in your browser to use the web app.
Step 3: Use the Web App
Enter the following inputs:
Age
Sex (Male=1, Female=0)
Cigarettes per day
Total Cholesterol
Systolic BP
Glucose

Click Predict

The app displays:

Heart Disease Risk (YES/NO)

Percentage probability of risk

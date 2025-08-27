Prepare my project folder
Heart_Disease_Prediction/
├── app.py
├── train_model.py
├── model.pkl
├── scaler.pkl 
└── templates/
└── index.html

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

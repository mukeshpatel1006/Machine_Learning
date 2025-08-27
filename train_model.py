import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
disease_df = pd.read_csv(r"C:\Users\Mukesh Patel\OneDrive\Desktop\machine_learning\framingham.csv")
disease_df.drop(columns=['education'], axis=1, inplace=True)
disease_df.rename(columns={'male':'Sex_male'}, inplace=True)

# Drop rows with NaN in features or target
disease_df = disease_df.dropna(subset=['age', 'Sex_male', 'cigsPerDay', 'totChol', 'sysBP', 'glucose', 'TenYearCHD'])

# Features & target
X = disease_df[['age', 'Sex_male', 'cigsPerDay', 'totChol', 'sysBP', 'glucose']].values
y = disease_df['TenYearCHD'].values

# Scale features
scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(X)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Save model and scaler
with open("model.pkl", "wb") as f:
    pickle.dump(logreg, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model and scaler saved successfully!")
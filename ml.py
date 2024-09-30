import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import csv

df = pd.read_csv("data.csv")
print(df)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df.sort_values(by='Date', inplace=True)

df.fillna(method='ffill', inplace=True)

df['Target'] = df['Blood Sugar Level (mg/dL)'].shift(-1)
df.dropna(inplace=True) 
X = df[['Blood Sugar Level (mg/dL)', 'Carbohydrate Intake (g)', 'Heart Rate (bpm)']]
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

def estimate_insulin_units(blood_sugar, carbohydrate_intake):
    base_units = max(0, (blood_sugar - 100) // 50) 
    carb_units = carbohydrate_intake // 10 
    total_units = base_units + carb_units
    return total_units

def get_blood_sugar_and_insulin_for_date(input_date):
    date_check = pd.to_datetime(input_date, format='%d-%m-%Y')
    if date_check in df['Date'].values:
        blood_sugar = df[df['Date'] == date_check]['Blood Sugar Level (mg/dL)'].values[0]
        carb_intake = df[df['Date'] == date_check]['Carbohydrate Intake (g)'].values[0]
        insulin_units = estimate_insulin_units(blood_sugar, carb_intake)
        return f"Blood Sugar Level for {input_date}: {blood_sugar} mg/dL, Insulin Units Needed: {insulin_units}"
    else:
        try:
            latest_data = df.iloc[-1][['Blood Sugar Level (mg/dL)', 'Carbohydrate Intake (g)', 'Heart Rate (bpm)']].values.reshape(1, -1)
            predicted_blood_sugar = model.predict(latest_data)[0]
            predicted_carb_intake = df['Carbohydrate Intake (g)'].mean()  # Average carb intake for estimation
            insulin_units = estimate_insulin_units(predicted_blood_sugar, predicted_carb_intake)
            return [input_date,predicted_blood_sugar,insulin_units]
        except:
            return [input_date,predicted_blood_sugar,insulin_units]
import pandas as pd
import joblib
import numpy as np

model = joblib.load("combinational_depth_model.pkl")

def predict_combinational_depth(data):
    
    df = pd.DataFrame([data], columns=["Num Gates", "Fan-In", "Fan-Out", "Logic Levels"])
    
  
    prediction = model.predict(df)
    
    return prediction[0]


test_data = {
    "Num Gates": 120,
    "Fan-In": 6,
    "Fan-Out": 3,
    "Logic Levels": 10
}

predicted_depth = predict_combinational_depth(test_data)
print(f"Predicted Combinational Depth: {predicted_depth}")

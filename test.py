import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load("combinational_depth_model.pkl")

# Function to test the model on new data
def predict_combinational_depth(data):
    # Convert data to DataFrame
    df = pd.DataFrame([data], columns=["Num Gates", "Fan-In", "Fan-Out", "Logic Levels"])
    
    # Predict
    prediction = model.predict(df)
    
    return prediction[0]

# Example: Test case (change values as needed)
test_data = {
    "Num Gates": 120,
    "Fan-In": 6,
    "Fan-Out": 3,
    "Logic Levels": 10
}

# Get prediction
predicted_depth = predict_combinational_depth(test_data)
print(f"Predicted Combinational Depth: {predicted_depth}")

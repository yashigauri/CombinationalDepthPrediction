import pandas as pd
import joblib
model = joblib.load("combinational_depth_model.pkl")
#One can use different data for prediction
sample_data = {
    "Num Gates": [120],
    "Fan-In": [6],
    "Fan-Out": [5],
    "Logic Levels": [9]
}
input_df = pd.DataFrame(sample_data)
prediction = model.predict(input_df)
print(f"Predicted Combinational Depth: {prediction[0]}")

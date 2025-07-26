import pandas as pd
import numpy as np
import pickle
from catboost import Pool, CatBoostRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import os

def load_model(model_path):
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def predict_depth():
    model_path = r"C:\Users\kksin\Documents\goc\yosys_project\results\combinational_depth_model.pkl"
    model = load_model(model_path)
    
    if model is None:
        return
    
    features = model.feature_names_
    print("\nFeatures used by the model:")
    for i, feature in enumerate(features):
        print(f"{i+1}. {feature}")
    
    print("\nPlease enter the circuit details:")
    
    input_data = {}
    
    circuit_name = input("Circuit name (e.g., 8bitALU): ")
    if not circuit_name.endswith(".sv"):
        circuit_name += ".sv"
    input_data["circuit_name"] = circuit_name
    
    for feature in features:
        if feature != "circuit_name":
            while True:
                try:
                    value = int(input(f"{feature}: "))
                    input_data[feature] = value
                    break
                except ValueError:
                    print("Please enter a valid number")
    
    input_df = pd.DataFrame([input_data])
    
    pred_pool = Pool(input_df, cat_features=["circuit_name"])
    
    prediction = model.predict(pred_pool)[0]
    
    print(f"\nPredicted combinational depth: {prediction:.2f}")
    
    update_model = input("\nDo you know the actual combinational depth? (y/n): ").lower()
    
    if update_model == 'y':
        while True:
            try:
                actual_depth = float(input("Please enter the actual combinational depth: "))
                break
            except ValueError:
                print("Please enter a valid number")
        
        save_new_data_point(input_df, actual_depth)
        
        error = abs(prediction - actual_depth)
        print(f"\nPrediction error: {error:.2f}")
        print("Data point has been saved and model is being retrained...")
        
        model = retrain_full_model()
        print("Model has been automatically retrained with the new data point.")
    
    another = input("\nWould you like to make another prediction? (y/n): ").lower()
    if another == 'y':
        predict_depth()

def save_new_data_point(input_df, actual_depth):
    dataset_path = r"C:\Users\kksin\Documents\goc\yosys_project\results\rtl_dataset.csv"
    
    if os.path.exists(dataset_path):
        existing_df = pd.read_csv(dataset_path, comment="#")
        
        new_row = input_df.copy()
        new_row["combinational_depth"] = actual_depth
        
        if "assignments" in existing_df.columns:
            new_row["assignments"] = actual_depth
        
        updated_df = pd.concat([existing_df, new_row], ignore_index=True)
        
        updated_df.to_csv(dataset_path, index=False)
        print(f"Dataset updated at: {dataset_path}")

def retrain_full_model():
    dataset_path = r"C:\Users\kksin\Documents\goc\yosys_project\results\rtl_dataset.csv"
    model_path = r"C:\Users\kksin\Documents\goc\yosys_project\results\combinational_depth_model.pkl"
    
    df = pd.read_csv(dataset_path, comment="#")
    
    categorical_features = ["circuit_name"]
    df["circuit_name"] = df["circuit_name"].astype(str)
    
    X = df.drop(columns=["combinational_depth"])
    y = df["combinational_depth"]
    
    train_pool = Pool(X, y, cat_features=categorical_features)
    
    model = CatBoostRegressor(
        iterations=1000,
        depth=6,
        learning_rate=0.1,
        loss_function="RMSE",
        verbose=50,
        random_seed=42
    )
    
    model.fit(train_pool)
    
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    
    return model

if __name__ == "__main__":
    print("=== Combinational Depth Prediction Tool ===")
    predict_depth()
    print("\nThank you for using the prediction tool!")
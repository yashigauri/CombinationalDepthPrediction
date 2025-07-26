import pandas as pd
import catboost
from catboost import CatBoostRegressor, Pool
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

try:
    dataset_path = "/home/yashigauri/yosys_project/results/rtl_dataset.csv"
    df = pd.read_csv(dataset_path, comment="#")

    # Drop unwanted column
    df = df.drop(columns=["circuit_name"])

    X = df.drop(columns=["combinational_depth"])
    y = df["combinational_depth"]

    # Split data for training and validation
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define CatBoost model
    model = CatBoostRegressor(
        iterations=500,
        depth=6,
        learning_rate=0.1,
        loss_function='RMSE',
        verbose=0
    )

    # Train model
    model.fit(X_train, y_train)

    # Evaluate on train and validation
    train_pred = model.predict(X_train)
    val_pred = model.predict(X_val)

    train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
    val_rmse = np.sqrt(mean_squared_error(y_val, val_pred))

    print(f"✅ Model trained successfully.")
    print(f"📉 Train RMSE: {train_rmse:.4f}")
    print(f"📊 Validation RMSE: {val_rmse:.4f}")

    # Save the model
    model_path = "/home/yashigauri/yosys_project/results/combinational_depth_model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"💾 Model saved at: {model_path}")

except Exception as e:
    print(f"❌ Error occurred: {e}")

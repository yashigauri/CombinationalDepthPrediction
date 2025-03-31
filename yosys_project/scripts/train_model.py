import pandas as pd
import numpy as np
import catboost
from catboost import CatBoostRegressor, Pool
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

dataset_path = r"C:\Users\kksin\Documents\goc\yosys_project\results\rtl_dataset.csv"
df = pd.read_csv(dataset_path, comment="#")

categorical_features = ["circuit_name"]
df["circuit_name"] = df["circuit_name"].astype(str)

X = df.drop(columns=["combinational_depth"])
y = df["combinational_depth"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

train_pool = Pool(X_train, y_train, cat_features=categorical_features)
test_pool = Pool(X_test, y_test, cat_features=categorical_features)

model = CatBoostRegressor(
    iterations=1000,
    depth=6,
    learning_rate=0.1,
    loss_function="RMSE",
    verbose=100,
    random_seed=42
)
model.fit(train_pool)

y_pred = model.predict(test_pool)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

model_path = r"C:\Users\kksin\Documents\goc\yosys_project\results\combinational_depth_model.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"Model trained and saved at: {model_path}")
print("Features used for training:", list(X.columns))

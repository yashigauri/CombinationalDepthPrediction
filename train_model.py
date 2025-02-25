import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("dataset_50_circuits.csv")


df = df.drop(columns=["Circuit Name"])


X = df.drop(columns=["Combinational Depth"])  
y = df["Combinational Depth"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")


import joblib
joblib.dump(model, "combinational_depth_model.pkl")
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("dataset_50_circuits.csv")


df = df.drop(columns=["Circuit Name"])

X = df.drop(columns=["Combinational Depth"])  
y = df["Combinational Depth"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


param_grid = {
    "n_estimators": [50, 100, 200],   
    "max_depth": [None, 5, 10],       
    "min_samples_split": [2, 5, 10]   
}

grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=5, scoring="neg_mean_absolute_error", n_jobs=-1)
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
print("Best Parameters:", grid_search.best_params_)

y_pred = best_model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")


joblib.dump(best_model, "combinational_depth_model.pkl")
print("Model saved as 'combinational_depth_model.pkl'")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("dataset_50_circuits.csv")

# Drop non-numeric column
df = df.drop(columns=["Circuit Name"])

# Split into features and target variable
X = df.drop(columns=["Combinational Depth"])  
y = df["Combinational Depth"]

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# Save the model
import joblib
joblib.dump(model, "combinational_depth_model.pkl")
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("dataset_50_circuits.csv")

# Drop non-numeric column
df = df.drop(columns=["Circuit Name"])

# Split into features and target variable
X = df.drop(columns=["Combinational Depth"])  
y = df["Combinational Depth"]

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define hyperparameter grid
param_grid = {
    "n_estimators": [50, 100, 200],   # Number of trees
    "max_depth": [None, 5, 10],       # Maximum depth of trees
    "min_samples_split": [2, 5, 10]   # Minimum samples to split a node
}

# Grid search with cross-validation
grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=5, scoring="neg_mean_absolute_error", n_jobs=-1)
grid_search.fit(X_train, y_train)

# Get best model
best_model = grid_search.best_estimator_
print("Best Parameters:", grid_search.best_params_)

# Predict with best model
y_pred = best_model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# Save the best model
joblib.dump(best_model, "combinational_depth_model.pkl")
print("Model saved as 'combinational_depth_model.pkl'")

import pickle
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor

model_path = "/home/yashigauri/yosys_project/results/combinational_depth_model.pkl"
dataset_path = "/home/yashigauri/yosys_project/results/rtl_dataset.csv"

with open(model_path, "rb") as f:
    model = pickle.load(f)

print("\nEnter circuit details:")

input_pins = int(input("Input Pins: "))
output_pins = int(input("Output Pins: "))
registers = int(input("Registers: "))
wires = int(input("Wires: "))
num_assignments = int(input("Number of Assignments: "))
assignments = int(input("Assignments: "))

new_data = np.array([[input_pins, output_pins, registers, wires, num_assignments, assignments]])

predicted_depth = model.predict(new_data)[0]
print(f"\nPredicted Combinational Depth: {predicted_depth:.2f}")

actual_depth = float(input("Enter actual combinational depth (if known, otherwise press Enter to skip): ") or -1)

if actual_depth != -1:
    df = pd.read_csv(dataset_path, comment="#")

    new_entry = pd.DataFrame([[input_pins, output_pins, registers, wires, num_assignments, assignments, actual_depth]],
                             columns=df.columns[1:])  

    df = pd.concat([df, new_entry], ignore_index=True)

    X = df.drop(columns=["combinational_depth"])
    y = df["combinational_depth"]

    model = CatBoostRegressor(iterations=500, depth=6, learning_rate=0.1, loss_function='RMSE', verbose=0)
    model.fit(X, y)

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    df.to_csv(dataset_path, index=False)

    print("\nModel updated with new data!")

print("\nDone.")



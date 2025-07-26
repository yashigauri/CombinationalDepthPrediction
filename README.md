# **Combinational Depth Prediction**  

This repository focuses on predicting the **combinational depth** of digital circuits using RTL descriptions and synthesis reports. The scripts in this directory facilitate feature extraction, synthesis, model training, and prediction.  

---

## **Repository Structure**  

### 📂 Verilog_Dataset/  
Contains Verilog (`.v`, `.sv`) files used for training and testing combinational depth prediction.  

### 📂 catboost_info/  
Stores metadata and training logs related to CatBoost, the machine learning model used for prediction.  

### 📂 yosys_env/  
Configuration and dependencies for running **Yosys**, the synthesis tool used for circuit analysis.  

---

## **Scripts Overview**  

### 📝 `checkfiles.py`  
Ensures all required files are correctly structured and checks for missing or corrupted data.  

### 📝 `extract_rtl_features.py`  
Extracts relevant RTL-based features from Verilog files, which are later used for model training.  

### 📝 `fix_file_structure.py`  
Organizes and standardizes file structures to maintain dataset consistency.  

### 📝 `predict_model.py`  
Loads the trained machine learning model and predicts the **combinational depth** of circuits based on extracted features.  

### 📝 `synthesis_script.ys`  
A **Yosys synthesis script** used to analyze and synthesize the Verilog circuits, generating reports on circuit depth and gate usage.  

### 📝 `train_model.py`  
Trains the CatBoost model using RTL features and synthesis data.  
🔹 Now prints both **training RMSE** and **validation RMSE** to evaluate model performance.  
🔹 The trained model is saved as a `.pkl` file for future predictions.  

### 📝 `tempCodeRunnerFile.py`  
Temporary scratch

# **Combinational Depth Prediction**  

This repository focuses on predicting the **combinational depth** of digital circuits using RTL descriptions and synthesis reports. The scripts in this directory facilitate feature extraction, synthesis, model training, and prediction.  

## **Repository Structure**  

### 📂 Verilog_Dataset/  
Contains Verilog (`.v`, `.sv`) files used for training and testing combinational depth prediction.  

### 📂 catboost_info/  
Stores metadata and training logs related to CatBoost, the machine learning model used for prediction.  

### 📂 yosys_env/  
Configuration and dependencies for running **Yosys**, the synthesis tool used for circuit analysis.  

---

## **Scripts Overview**  

### 📝 **checkfiles.py**  
Ensures all required files are correctly structured and checks for missing or corrupted data.  

### 📝 **extract_rtl_features.py**  
Extracts relevant RTL-based features from Verilog files, which are later used for model training.  

### 📝 **fix_file_structure.py**  
Organizes and standardizes file structures to maintain dataset consistency.  

### 📝 **predict_model.py**  
Loads the trained machine learning model and predicts the **combinational depth** of circuits based on extracted features.  

### 📝 **synthesis_script.ys**  
A **Yosys synthesis script** used to analyze and synthesize the Verilog circuits, generating reports on circuit depth and gate usage.  

### 📝 **tempCodeRunnerFile.py**  
A temporary file used for testing or debugging scripts during execution.  

### 📝 **train_model.py**  
Trains the CatBoost model using extracted RTL features and synthesis data, optimizing for combinational depth prediction.  

---

## **Usage**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yashigauri/CombinationalDepthPrediction.git
   cd CombinationalDepthPrediction/yosys_project/scripts
   ```  
2. Extract features from Verilog files:  
   ```bash
   python extract_rtl_features.py
   ```  
3. Run synthesis using Yosys:  
   ```bash
   yosys synthesis_script.ys
   ```  
4. Train the model:  
   ```bash
   python train_model.py
   ```  
5. Predict combinational depth:  
   ```bash
   python predict_model.py
   ```  




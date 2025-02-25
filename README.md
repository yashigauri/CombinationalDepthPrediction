# Combinational Logic Depth Prediction 🚀  

This project uses **Machine Learning** to predict the **combinational logic depth** of signals in an RTL module without requiring a full synthesis run.  
It speeds up **timing analysis** by identifying potential **timing violations** early in the design process.  

## 📌 Problem Statement  
Timing analysis is **time-consuming** since it relies on synthesis reports. This project creates an **AI-based model** to predict the **combinational depth** of signals, reducing dependency on synthesis tools and optimizing **design flow efficiency**.  

---  

## 📂 Project Structure  
- **dataset_50_circuits.csv** → Dataset containing circuit parameters and actual combinational depths.  
- **train_model.py** → ML model that trains a **RandomForestRegressor** to predict logic depth.  
- **combinational_depth_model.pkl** → Saved trained model for predictions.  
- **predict.py** → Script to predict combinational depth for new circuits using the trained model.  
- **README.md** → This documentation.  
- **test.py** → Using test data. 

---  

## 🚀 How to Run the Project  
1. **Clone the Repository:**  
   ```sh  
   git clone https://github.com/yashigauri/CombinationalDepthPrediction.git  
   cd CombinationalDepthPrediction  
   ```  
2. **Install Dependencies:**  
   ```sh  
   pip install -r requirements.txt  
   ```  
3. **Train the Model:**  
   ```sh  
   python train_model.py  
   ```  
4. **Make Predictions:**  
   ```sh  
   python predict.py  
   ```  

## 📌 Future Improvements  
- Improve feature selection for better accuracy.  
- Explore Deep Learning models for further optimization.  

---



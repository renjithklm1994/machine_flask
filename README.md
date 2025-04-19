# machine_flask

Here's a clean and professional version of your **README** section that describes your house price prediction project:

---

## House Price Prediction Model

This project aims to predict house prices based on key features like location, square footage, number of bedrooms (BHK), and bathrooms. It includes a full pipeline from data preprocessing to model deployment with a simple web interface.

### Features

- **Data Cleaning & Feature Engineering**  
  - Removed outliers to improve data quality  
  - Created meaningful features for better model performance  

- **Model Training & Evaluation**  
  - Tried different models: **Linear Regression**, **Decision Tree**, and **Lasso Regression**  
  - Used **GridSearchCV** with **K-Fold Cross-Validation** to tune hyperparameters and select the best model  

- **Model Export**  
  - Final model saved using **Pickle** as a `.pkl` file  

- **Flask API**  
  - Created a RESTful API using **Flask** to serve the model for predictions  

- **Frontend Integration**  
  - Built a simple UI using **HTML**, **CSS**, and **JavaScript**  
  - Takes user inputs (location, sqft, BHK, bath) and returns the predicted price  


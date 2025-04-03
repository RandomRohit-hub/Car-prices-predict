# 🚗 Car Selling Price Predictor

https://car-prices-predict-7cpqsd88e4vgjymmbykqwf.streamlit.app/



## 📌 Overview
The **Car Selling Price Predictor** is a Streamlit-based web app that estimates the selling price of a car based on user inputs such as car name, fuel type, year of manufacture, and other factors. The model is trained using a **Random Forest Regressor** on a dataset of car dealership data.

## 🔧 Features
- **Interactive UI** with dropdowns and input fields.
- **Real-time predictions** based on machine learning.
- **Image support** for selected car brands.
- **Standardized preprocessing** for better predictions.

## 🚀 How to Run
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 2️⃣ Run the App
```bash
streamlit run app.py
```

## 📁 Dataset
The model is trained on `car_dealership_data_50.csv`, which includes features like:
- `Car Name`
- `Year`
- `Present Price`
- `KMs Driven`
- `Fuel Type`
- `Seller Type`
- `Transmission`
- `Owner`
- `Selling Price` (Target Variable)

## 🏗 Model & Preprocessing
- **Categorical Features**: Encoded using `LabelEncoder`.
- **Numerical Features**: Scaled using `StandardScaler`.
- **Model Used**: `RandomForestRegressor` from `scikit-learn`.

## 🔥 Deployment
To deploy on **Streamlit Cloud**, ensure you have:
- `requirements.txt` with dependencies.
- The dataset (`car_dealership_data_50.csv`) included.
- Streamlit account linked to your GitHub repository.

## 🛠 Tech Stack
- **Python**
- **Streamlit** (Frontend & Deployment)
- **Pandas** (Data Handling)
- **Scikit-learn** (Machine Learning)
- **Joblib** (Model Serialization)

## 🎯 Future Improvements
- Add more car brands & images.
- Improve model accuracy with feature engineering.
- Deploy as a web service with FastAPI.

## 📜 License
This project is licensed under the **MIT License**.


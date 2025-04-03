import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Set Streamlit page configuration (must be at the top)
st.set_page_config(page_title="Car Selling Price Predictor", page_icon="🚗", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("car_dealership_data_50.csv")
    return df

df = load_data()

# Preprocessing
categorical_cols = ["Car Name", "Fuel Type", "Seller Type", "Transmission"]
numerical_cols = ["Year", "Present Price", "Kms Driven", "Owner"]

df_encoded = df.copy()
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df[col])
    label_encoders[col] = le

scaler = StandardScaler()
df_encoded[numerical_cols] = scaler.fit_transform(df[numerical_cols])

X = df_encoded.drop(columns=["Selling Price"])
y = df_encoded["Selling Price"]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Streamlit UI
st.markdown("""
    <style>
    .big-font {font-size:30px !important; font-weight: bold; text-align: center;}
    </style>
    """, unsafe_allow_html=True)

st.title("🚗 Car Selling Price Predictor")
st.markdown("<p class='big-font'>Enter Car Details to Estimate Selling Price</p>", unsafe_allow_html=True)

# Load car brand images
def get_car_image(brand):
    images = {
        "Honda": "https://wallpapercave.com/wp/886foH2.jpg",
        "Toyota": "https://th.bing.com/th/id/R.28af9f9e7d9a24312579eeb763670105?rik=EGbHSeRlSRNBmg&riu=http%3a%2f%2fpluspng.com%2fimg-png%2ftoyota-symbol-3408.jpg&ehk=fqmiBj8j0akDKcoZMkg%2bvTvKjXnBBEqnt%2bA5c2ouOOc%3d&risl=&pid=ImgRaw&r=0",
        "Ford": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Ford_logo_flat.svg/512px-Ford_logo_flat.svg.png",
        "BMW": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/BMW.svg/512px-BMW.svg.png"
    }
    return images.get(brand.split()[0], "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Red_Car.svg/512px-Red_Car.svg.png")

col1, col2 = st.columns([1, 2])

with col1:
    car_name = st.selectbox("Car Name", df["Car Name"].unique())
    st.image(get_car_image(car_name), width=150)

with col2:
    year = st.number_input("Year", min_value=2000, max_value=2025, step=1)
    present_price = st.number_input("Present Price (Lakhs)", min_value=0.0, step=0.1)
    kms_driven = st.number_input("KMs Driven", min_value=0, step=100)
    fuel_type = st.selectbox("Fuel Type", df["Fuel Type"].unique())
    seller_type = st.selectbox("Seller Type", df["Seller Type"].unique())
    transmission = st.selectbox("Transmission", df["Transmission"].unique())
    owner = st.number_input("Owner (0: First, 1: Second, etc.)", min_value=0, max_value=3, step=1)

# Convert user input into model format
input_data = pd.DataFrame([[car_name, year, present_price, kms_driven, fuel_type, seller_type, transmission, owner]],
                          columns=["Car Name", "Year", "Present Price", "Kms Driven", "Fuel Type", "Seller Type", "Transmission", "Owner"])

for col in categorical_cols:
    input_data[col] = label_encoders[col].transform(input_data[col])

input_data[numerical_cols] = scaler.transform(input_data[numerical_cols])

# Predict price
if st.button("🔍 Predict Selling Price", use_container_width=True):
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Selling Price: ₹{prediction[0]:,.2f} Lakhs")
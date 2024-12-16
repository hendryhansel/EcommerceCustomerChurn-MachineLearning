import streamlit as st
import pickle
import numpy as np

# Load Model
model_filename = 'C:\\Users\\EDITH\\Documents\\Python Scripts\\hendrymodel.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# App Title
st.title("E-commerce Customer Churn Prediction")

# Input Fields
st.header("Masukkan Informasi Pelanggan")
tenure = st.number_input("Tenure (bulan)", min_value=0, value=12)
warehouse_to_home = st.number_input("Jarak Warehouse ke Rumah (km)", min_value=0, value=5)
number_of_devices = st.number_input("Jumlah Perangkat Terdaftar", min_value=1, value=1)
preferred_order_cat = st.selectbox("Kategori Pesanan Favorit", ["Fashion", "Mobile", "Laptop & Accessory", "Others"])
satisfaction_score = st.slider("Nilai Kepuasan (1-5)", 1, 5, 3)
marital_status = st.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"])
number_of_address = st.number_input("Jumlah Alamat", min_value=1, value=1)
complain = st.selectbox("Apakah ada keluhan?", ["Ya", "Tidak"])
days_since_last_order = st.number_input("Hari Sejak Pesanan Terakhir", min_value=0, value=7)
cashback_amount = st.number_input("Jumlah Cashback Bulanan (USD)", min_value=0.0, value=50.0)

# Encoding Kategori
preferred_order_cat_map = {"Fashion": 0, "Mobile": 1, "Laptop & Accessory": 2, "Others": 3}
marital_status_map = {"Single": 0, "Married": 1, "Divorced": 2}
complain_map = {"Ya": 1, "Tidak": 0}

inputs = np.array([[
    tenure,
    warehouse_to_home,
    number_of_devices,
    preferred_order_cat_map[preferred_order_cat],
    satisfaction_score,
    marital_status_map[marital_status],
    number_of_address,
    complain_map[complain],
    days_since_last_order,
    cashback_amount
]])

# Predict Button
if st.button("Prediksi"):
    prediction = model.predict(inputs)
    if prediction[0] == 1:
        st.error("Pelanggan kemungkinan akan churn!")
    else:
        st.success("Pelanggan tidak akan churn!")

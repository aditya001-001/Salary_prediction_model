
import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("salary_model.pkl")

# Configure the webpage
st.set_page_config(page_title="Salary Predictor", page_icon="💰")

st.title("💰 Salary Prediction App")
st.write("Predict your salary based on your years of experience.")

# Get input from the user
experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.1
)

# Predict salary when the button is clicked
if st.button("Predict Salary"):
    input_data = pd.DataFrame({
        "YearsExperience": [experience]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Salary: {prediction:,.2f}")

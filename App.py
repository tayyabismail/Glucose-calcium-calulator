import streamlit as st
import numpy as np

# Function to calculate estimated HbA1c
def calculate_hba1c(average_glucose):
    # The formula for estimating HbA1c from average glucose is:
    # HbA1c (%) = (average_glucose (mg/dL) + 46.7) / 28.7
    estimated_hba1c = (average_glucose + 46.7) / 28.7
    return round(estimated_hba1c, 2)

# Function to provide health advice based on glucose levels
def provide_health_advice(glucose_level):
    if glucose_level < 70:
        return "Your blood glucose level is low (hypoglycemia). Please consult a healthcare provider and consider consuming fast-acting carbohydrates like juice or glucose tablets."
    elif 70 <= glucose_level <= 99:
        return "Your blood glucose level is within the normal range. Keep up the good work!"
    elif 100 <= glucose_level <= 125:
        return "Your blood glucose level is elevated (pre-diabetes). Consider lifestyle changes like diet and exercise, and consult a healthcare provider for further advice."
    else:
        return "Your blood glucose level is high (diabetes or hyperglycemia). Please consult a healthcare provider for advice and potential medication adjustments."

# Streamlit App
st.title("Blood Glucose and HbA1c Assessment")

# Collect blood glucose input from the user
glucose_level = st.number_input("Enter your blood glucose level (mg/dL):", min_value=0.0, step=0.1)

if glucose_level:
    # Display health advice
    advice = provide_health_advice(glucose_level)
    st.write(f"Health Advice: {advice}")

    # Estimate HbA1c based on the glucose level
    estimated_hba1c = calculate_hba1c(glucose_level)
    st.write(f"Estimated HbA1c: {estimated_hba1c} %")

# Optionally, provide educational content
st.subheader("What is HbA1c?")
st.write("""
HbA1c is a blood test that measures your average blood sugar levels over the past 2-3 months. It is often used to diagnose and monitor diabetes. The normal HbA1c level is below 5.7%. Higher values indicate pre-diabetes or diabetes.
""")

st.subheader("Glucose Ranges")
st.write("""
- **Normal**: 70-99 mg/dL
- **Pre-diabetes**: 100-125 mg/dL
- **Diabetes**: 126 mg/dL or higher
""")

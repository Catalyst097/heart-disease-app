import streamlit as st
import pandas as pd
import joblib

pipeline = joblib.load("model.pkl")

st.title("Heart Disease Risk Predictor")
st.write("Enter patient details to predict heart disease risk.")
st.caption("⚠️ Educational demo only — not medical advice.")

age = st.number_input("Age", 20, 100, 50)

sex = st.selectbox(
    "Sex", [1, 0],
    format_func=lambda x: "Male" if x == 1 else "Female"
)

cp = st.selectbox(
    "Chest Pain Type", [0, 1, 2, 3],
    format_func=lambda x: {
        0: "Typical Angina",
        1: "Atypical Angina",
        2: "Non-anginal Pain",
        3: "Asymptomatic"
    }[x]
)

trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)

chol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl", [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

restecg = st.selectbox(
    "Resting ECG Results", [0, 1, 2],
    format_func=lambda x: {
        0: "Normal",
        1: "ST-T Wave Abnormality",
        2: "Left Ventricular Hypertrophy"
    }[x]
)

thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)

exang = st.selectbox(
    "Exercise Induced Angina", [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 10.0, 1.0, step=0.1)

slope = st.selectbox(
    "Slope of Peak Exercise ST Segment", [0, 1, 2],
    format_func=lambda x: {
        0: "Upsloping",
        1: "Flat",
        2: "Downsloping"
    }[x]
)

ca = st.selectbox(
    "Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3]
)

thal = st.selectbox(
    "Thalassemia", [0, 1, 2, 3],
    format_func=lambda x: {
        0: "Unknown",
        1: "Normal",
        2: "Fixed Defect",
        3: "Reversible Defect"
    }[x]
)

if st.button("Predict"):
    input_df = pd.DataFrame([{
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps, "chol": chol,
        "fbs": fbs, "restecg": restecg, "thalach": thalach, "exang": exang,
        "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
    }])
    prediction = pipeline.predict(input_df)[0]
    result = "⚠️ Heart Disease Likely" if prediction == 1 else "✅ No Heart Disease Indicated"
    st.subheader(result)
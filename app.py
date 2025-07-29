import streamlit as st
import numpy as np
import pickle
import xgboost as xgb
import os

model = xgb.XGBClassifier()
model.load_model(os.path.join("models", "model.json"))

scaler = pickle.load(open(os.path.join("models", "scaler.pkl"), "rb"))

def get_diabetes_tips():
    return [
        "🥗 Eat more fiber and whole grains.",
        "🚶 Exercise at least 30 minutes daily.",
        "🧘 Manage your stress.",
        "🩺 Visit your doctor regularly.",
        "🚭 Stop smoking if you do.",
        "⚖️ Maintain a healthy weight.",
        "💧 Drink plenty of water instead of sugary drinks."
    ]

def display_tips():
    st.markdown("### 💡 Health Tips")
    for tip in get_diabetes_tips():
        st.markdown(f"- {tip}")

st.markdown("<h1 style='text-align: center'>🩺 Diabetes Prediction </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Enter patient information below to predict diabetes risk</h4>", unsafe_allow_html=True)

st.markdown("### Patient Information")
col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input("👶 Pregnancies", min_value=0, max_value=100, value=1)
    glucose = st.number_input("🩸 Glucose Level", min_value=70, max_value=200, value=110)
    blood_pressure = st.number_input("💓 Blood Pressure", min_value=40, max_value=130, value=70)
    skin_thickness = st.number_input("📏 Skin Thickness", min_value=10, max_value=100, value=20)
with col2:
    insulin = st.number_input("💉 Insulin Level", min_value=10, max_value=300, value=79)
    bmi = st.number_input("⚖️ BMI", min_value=15.0, max_value=70.0, value=32.0, step=0.1)
    dpf = st.number_input("🧬 DPF", min_value=0.0, max_value=3.0, value=0.372, step=0.001)
    age = st.number_input("🎂 Age", min_value=1, max_value=100, value=33)

st.markdown("---")
if st.button("🔍 Predict Diabetes Risk", use_container_width=True):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)



    if prediction[0] == 1:
        st.error("⚠️ This person **is at risk** of diabetes.")
        col1, col2 = st.columns([2, 1])
        with col1:
            display_tips()
        with col2:
            st.image("images\Gemini_Generated_Image_cvsmkkcvsmkkcvsm-Picsart-AiImageEnhancer-removebg-preview.png", width=200 )
    else:
        st.success("✅ This person **is not at risk** of diabetes.")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### 🎉 Great News!")
            st.markdown("**💪 You are healthy! Keep up your healthy lifestyle.**")
            st.markdown("""
                <div style='font-size:18px;'>
                - 🥗 Continue eating nutritious food  <br>
                - 🚶 Stay active every day  <br>
                - 💧 Drink plenty of water  <br>
                - 😴 Get enough sleep  <br>
                - 💖 Your body will thank you!
                </div>
                """, unsafe_allow_html=True)

        with col2:
            st.image("images/download__1_-removebg-preview.png", width=160)

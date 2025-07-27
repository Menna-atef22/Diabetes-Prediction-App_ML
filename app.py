#cd C:\Users\menna\Downloads\Diabetes_Prediction_App
#streamlit run "app.py"




import streamlit as st
import numpy as np
import pickle

# تحميل الموديل
model = pickle.load(open("model.pkl", "rb"))

# إضافة صورة
st.image("https://cdn-icons-png.flaticon.com/512/3875/3875173.png", width=100)  # يمكنك تغيير الرابط لصورة من اختيارك

# عنوان التطبيق
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🩺 Diabetes Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Enter patient information below to predict diabetes risk</h4>", unsafe_allow_html=True)

# تقسيم الإدخالات لمجموعات
st.markdown("### Patient Information")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("👶 Pregnancies", min_value=0, max_value=20, value=1, step=1)
    glucose = st.number_input("🩸 Glucose Level", min_value=0, max_value=200, value=110, step=1)
    blood_pressure = st.number_input("💓 Blood Pressure", min_value=0, max_value=140, value=70, step=1)
    skin_thickness = st.number_input("📏 Skin Thickness", min_value=0, max_value=100, value=20, step=1)

with col2:
    insulin = st.number_input("💉 Insulin Level", min_value=0, max_value=800, value=79, step=1)
    bmi = st.number_input("⚖️ BMI", min_value=0.0, max_value=70.0, value=32.0, step=0.1, format="%.1f")
    dpf = st.number_input("🧬 DPF", min_value=0.0, max_value=2.5, value=0.372, step=0.001, format="%.3f")
    age = st.number_input("🎂 Age", min_value=1, max_value=100, value=33, step=1)

# زر التنبؤ
st.markdown("---")
if st.button("🔍 Predict Diabetes Risk", use_container_width=True):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ This person **is at risk** of diabetes.")
    else:
        st.success("✅ This person **is not at risk** of diabetes.")

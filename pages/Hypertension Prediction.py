import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open("pages\models\hypertension.pkl", "rb") as f:
    model = pickle.load(f)


def preprocess_input(
    age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
):
    sex = int(sex)
    cp = int(cp)
    fbs = int(fbs)
    restecg = int(restecg)
    exang = int(exang)
    slope = int(slope)
    ca = int(ca)
    thal = int(thal)

    return [
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal,
    ]


st.markdown(
    """
    <h2><u>Answer the Questionnaire to know your chances of having Hypertension.</u></h2>
    """,
    unsafe_allow_html=True,
)

age = st.number_input("Age", min_value=0, max_value=150, step=1)
sex = st.selectbox("Sex", ["Female", "Male"])
cp = st.selectbox(
    "Chest Pain Type",
    ["Asymptomatic", "Typical Angina", "Atypical Angina", "Non-Anginal Pain"],
)
trestbps = st.number_input(
    "Resting Blood Pressure (mm Hg)", min_value=0, max_value=250, step=1
)
chol = st.number_input("Serum Cholestoral (mg/dl)", min_value=0, max_value=600, step=1)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
restecg = st.selectbox(
    "Resting ECG Results",
    ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"],
)
thalach = st.number_input(
    "Maximum Heart Rate Achieved", min_value=0, max_value=250, step=1
)
exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input(
    "ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1
)
slope = st.selectbox(
    "Slope of Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"]
)
ca = st.number_input(
    "Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=3, step=1
)
thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

sex = 1 if sex == "Male" else 0
cp_mapping = {
    "Asymptomatic": 0,
    "Typical Angina": 1,
    "Atypical Angina": 2,
    "Non-Anginal Pain": 3,
}
cp = cp_mapping[cp]
fbs = 1 if fbs == "Yes" else 0
restecg_mapping = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2,
}
restecg = restecg_mapping[restecg]
exang = 1 if exang == "Yes" else 0
slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
slope = slope_mapping[slope]
thal_mapping = {"Normal": 3, "Fixed Defect": 6, "Reversible Defect": 7}
thal = thal_mapping[thal]

if st.button("Submit"):
    input_data = {
        "age": np.array([age]),
        "sex": np.array([sex]),
        "cp": np.array([cp]),
        "trestbps": np.array([trestbps]),
        "chol": np.array([chol]),
        "fbs": np.array([fbs]),
        "restecg": np.array([restecg]),
        "thalach": np.array([thalach]),
        "exang": np.array([exang]),
        "oldpeak": np.array([oldpeak]),
        "slope": np.array([slope]),
        "ca": np.array([ca]),
        "thal": np.array([thal]),
    }
    df = pd.DataFrame(input_data)
    predictions = model.predict(df)
    if predictions[0]:
        st.write("Yes are chances of you to have hypertension you could follow some precautions")
        if age <= 18:
            st.markdown("## Hypertension for Childhood and Adolescence (Ages 0-18):")
            st.markdown("- Encourage a healthy diet with limited salt intake.")
            st.markdown("- Promote physical activity and discourage sedentary behaviors.")
            st.markdown("- Monitor blood pressure periodically, especially if there's a family history of hypertension.")

        elif 19 <= age <= 39:
            st.markdown("## Hypertension for Young Adulthood (Ages 19-39):")
            st.markdown("- Maintain a healthy weight through diet and exercise.")
            st.markdown("- Limit alcohol consumption and avoid smoking.")
            st.markdown("- Monitor blood pressure regularly, especially if there's a family history of hypertension.")

        elif 40 <= age <= 64:
            st.markdown("## Hypertension for Middle Adulthood (Ages 40-64):")
            st.markdown("- Schedule regular blood pressure checks and follow medical advice.")
            st.markdown("- Reduce stress through relaxation techniques and hobbies.")
            st.markdown("- Adopt a heart-healthy diet low in sodium and high in fruits, vegetables, and whole grains.")

        else:
            st.markdown("## Hypertension for Older Adulthood (Ages 65+):")
            st.markdown("- Continue with regular blood pressure monitoring and medication adherence.")
            st.markdown("- Be cautious with over-the-counter medications that may affect blood pressure.")
            st.markdown("- Stay physically active and maintain a healthy weight to manage hypertension effectively.")
    else:
        st.write(
            "No , there no chances of you to have hypertension but you could follow some prevention"
        )
        if age <= 18:
            st.markdown("## Prevention of Hypertension for Childhood and Adolescence (Ages 0-18):")
            st.markdown("- Encourage a diet rich in fruits, vegetables, and whole grains while limiting processed foods and excessive salt intake.")
            st.markdown("- Promote regular physical activity and limit sedentary behaviors.")
            st.markdown("- Educate about the importance of maintaining a healthy weight and avoiding obesity.")
            st.markdown("- Monitor blood pressure regularly, especially if there's a family history of hypertension.")

        elif 19 <= age <= 39:
            st.markdown("## Prevention of Hypertension for Young Adulthood (Ages 19-39):")
            st.markdown("- Maintain a healthy weight through balanced nutrition and regular exercise.")
            st.markdown("- Limit alcohol consumption and avoid smoking.")
            st.markdown("- Manage stress through relaxation techniques like yoga, meditation, or deep breathing exercises.")
            st.markdown("- Monitor blood pressure regularly, especially if there are risk factors present such as obesity or a family history of hypertension.")

        elif 40 <= age <= 64:
            st.markdown("## Prevention of Hypertension for Middle Adulthood (Ages 40-64):")
            st.markdown("- Adopt heart-healthy eating habits, focusing on low-sodium foods, lean proteins, and potassium-rich fruits and vegetables.")
            st.markdown("- Engage in regular aerobic exercise and strength training to improve cardiovascular health.")
            st.markdown("- Get regular check-ups to monitor blood pressure and other risk factors for hypertension.")
            st.markdown("- Manage stress effectively through healthy coping mechanisms and stress-reduction techniques.")

        else:
            st.markdown("## Prevention of Hypertension for Older Adulthood (Ages 65+):")
            st.markdown("- Maintain a healthy lifestyle with regular physical activity, balanced nutrition, and adequate hydration.")
            st.markdown("- Monitor blood pressure regularly and adhere to prescribed medications.")
            st.markdown("- Be cautious with over-the-counter medications and supplements that may affect blood pressure.")
            st.markdown("- Stay socially connected and engaged in activities to support mental and emotional well-being.")

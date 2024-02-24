import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pickle
import pandas as pd

with open("pages\models\heart_attack_xgboost.pkl", "rb") as f:
    model = pickle.load(f)


def change_to_bin(ans: str):
    if ans == "Yes" or ans == "Male":
        return 1
    else:
        return 0


st.set_page_config(
    page_title="Heart attack",
    page_icon="👋",
)

st.markdown(
    """
    <h2><u>Answer the Questionnaire to know your chances of getting Heart attack.</u></h2>
""",
    unsafe_allow_html=True,
)
age = st.number_input("Enter Your Age")

gender = st.radio(
    "Gender :",
    options=["Male", "Female"],
    index=0,
    format_func=str.capitalize,
)

chol = st.number_input("Cholesterol levels", key="chol_input")

blood_pressure_systolic = st.number_input(
    "Systolic Blood Pressure (120/80 mmHg: -> Systolic Blood Pressure is 120)"
)
blood_pressure_diastolic = st.number_input(
    "Diastolic Blood Pressure (120/80 mmHg: -> Diastolic Blood Pressure is 80)"
)


heart_rate = st.number_input("Heart Rate")

diabetes = st.radio("Diabetes", ["Yes", "No"])


family_history = st.radio("Family history of heart-related problems", ["Yes", "No"])


smoking = st.radio("Do you Smoke", ["Yes", "No"])

obesity = st.radio("Obesity", ["Yes", "No"])


alcohol_consumption = st.selectbox(
    "Alcohol consumption", ["Yes", "No"])


exercise_hours = st.number_input("Exercise Hours Per Week")


diet = st.selectbox("Dietary habits", ["Healthy", "Average", "Unhealthy"])


previous_heart_problems = st.radio("Previous heart problems", ["Yes", "No"])


medication_use = st.radio("Medication usage", ["Yes", "No"])


stress_level = st.slider("Stress level (1-10)", 1, 10)


sedentary_hours = st.number_input("Hours of sedentary activity per day")


bmi = st.number_input("Body Mass Index (BMI)")

triglycerides = st.number_input("Triglyceride levels")


physical_activity_days = st.number_input("Days of physical activity per week")


sleep_hours = st.number_input("Hours of sleep per day")

countries = [
    "Argentina",
    "Canada",
    "France",
    "Thailand",
    "Germany",
    "Japan",
    "Brazil",
    "South Africa",
    "United States",
    "Vietnam",
    "China",
    "Italy",
    "Spain",
    "India",
    "Nigeria",
    "New Zealand",
    "South Korea",
    "Australia",
    "Colombia",
    "United Kingdom",
]

country = st.selectbox("Country", countries)


submit_button = st.button("Submit")

if submit_button:
    data_dictionary = {
        "Age": np.array([age]),
        "Sex": np.array([gender]),
        "Cholesterol": np.array([chol]),
        "Heart Rate": np.array([heart_rate]),
        "Diabetes": np.array([diabetes]),
        "Family History": np.array([family_history]),
        "Smoking": np.array([smoking]),
        "Obesity": np.array([change_to_bin(obesity)]),
        "Alcohol Consumption": np.array([change_to_bin(alcohol_consumption)]),
        "Exercise Hours Per Week": np.array([exercise_hours]),
        "Diet": np.array([diet]),
        "Previous Heart Problems": np.array([change_to_bin(previous_heart_problems)]),
        "Medication Use": np.array([change_to_bin(medication_use)]),
        "Stress Level": np.array([stress_level]),
        "Sedentary Hours Per Day": np.array([sedentary_hours]),
        "BMI": np.array([bmi]),
        "Triglycerides": np.array([triglycerides]),
        "Physical Activity Days Per Week": np.array([physical_activity_days]),
        "Sleep Hours Per Day": np.array([sleep_hours]),
        "Country": np.array([country]),
        "Systolic": np.array([blood_pressure_systolic]),
        "Diastolic": np.array([blood_pressure_diastolic]),
    }
    df = pd.DataFrame(data_dictionary)
    # print("Number of features in df before transformation:", df.shape[1])
    cat_col = df.select_dtypes(include=object).columns.tolist()
    ct = ColumnTransformer(
        transformers=[
            ("encoder", OneHotEncoder(), cat_col)
        ],
        remainder="passthrough",
    )
    pred_out = ct.fit_transform(df)
    # print("Number of features in df after transformation:", pred_out.shape[1])
    # pred = model.predict(pred_out)
    st.write(pred_out)
    st.write(df)

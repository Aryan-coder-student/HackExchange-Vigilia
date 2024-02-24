import streamlit as st
import numpy as np
import pandas as pd
import pickle

with open("pages/models/diabeties_xgboost.pkl", "rb") as f:
    xgb_model = pickle.load(f)

st.markdown(
    """
    <h2><u>Answer the Questionnaire to know your chances of having Diabetes.</u></h2>
    """,
    unsafe_allow_html=True,
)


def change_to_bin(ans:str):
    if (ans=="Yes" or ans=="Male"):
        return 1
    else:
        return 0

def yes_no_input(label, key=None):
    return st.radio(label, options=["Yes", "No"], key=key)


high_chol = yes_no_input("Do you have high Cholestrol", key="high_chol")


age = st.number_input("Age", min_value=0.0, value=20.0, step=1.0, key="age")


chol_check = yes_no_input(
    "Have you had a cholesterol check in the past 5 years?", key="chol_check"
)


bmi = st.number_input("BMI", min_value=0.0, value=20.0, step=0.1, key="bmi")


smoker = yes_no_input(
    "Have you smoked at least 100 cigarettes in your entire life?", key="smoker"
)


heart_disease_attack = yes_no_input(
    "Heart Disease or Heart Attack", key="heart_disease_attack"
)


phys_activity = yes_no_input(
    "Have you engaged in physical activity in the past 30 days (not including job)?",
    key="phys_activity",
)


fruits = yes_no_input("Do you consume fruit 1 or more times per day?", key="fruits")


veggies = yes_no_input(
    "Do you consume vegetables 1 or more times per day?", key="veggies"
)


hvy_alcohol_consump = yes_no_input(
    "Do you consume alcohol ? (Adult men >=14 drinks per week and adult women >=7 drinks per week) ",
    key="hvy_alcohol_consump",
)


health_rating = st.select_slider(
    "How would you rate your general health?",
    options=[1, 2, 3, 4, 5],
    key="health_rating",
)


mental_health_days = st.slider(
    "Number of days of poor mental health in the past 30 days",
    min_value=1,
    max_value=30,
    key="mental_health_days",
)


phys_hlth = yes_no_input(
    "Have you experienced physical illness or injury in the past 30 days?",
    key="phys_hlth",
)


diff_walk = yes_no_input(
    "Do you have serious difficulty walking or climbing stairs?", key="diff_walk"
)


stroke = yes_no_input("Have you ever had a stroke?", key="stroke")


high_bp = yes_no_input("Do you have high blood pressure?", key="high_bp")


gender = st.radio("Gender", options=["Male", "Female"], key="sex")


submit_button = st.button("Submit")


if submit_button:
    sample_data = {
        "Age": np.array([age]),
        "Sex": np.array([change_to_bin(gender)]),
        "HighChol": np.array([change_to_bin(high_chol)]),
        "CholCheck": np.array([change_to_bin(chol_check)]),
        "BMI": np.array([bmi]),
        "Smoker": np.array([change_to_bin(smoker)]),
        "HeartDiseaseorAttack": np.array([change_to_bin(heart_disease_attack)]),
        "PhysActivity": np.array([change_to_bin(phys_activity)]),
        "Fruits": np.array([change_to_bin(fruits)]),
        "Veggies": np.array([change_to_bin(veggies)]),
        "HvyAlcoholConsump": np.array([change_to_bin(hvy_alcohol_consump)]),
        "GenHlth": np.array([change_to_bin(health_rating)]),
        "DiffWalk": np.array([change_to_bin(diff_walk)]),
        "Stroke": np.array([change_to_bin(stroke)]),
        "HighBP": np.array([change_to_bin(high_bp)]),
    }

    df = pd.DataFrame(sample_data)
    predictions = xgb_model.predict(df)

    if predictions[0]:
        st.write("Yes there are chances to have diabetes but should follow these check points : ")
        if age <= 18:
            st.markdown("## Diabetes for Childhood and Adolescence (Ages 0-18):")
            st.markdown("- Encourage a balanced diet with controlled sugar intake.")
            st.markdown("- Promote regular physical activity to maintain a healthy weight and improve insulin sensitivity.")
            st.markdown("- Monitor blood sugar levels regularly, especially for those at risk.")

        elif 19 <= age <= 39:
            st.markdown("## Diabetes for Young Adulthood (Ages 19-39):")
            st.markdown("- Maintain a healthy weight through diet and exercise.")
            st.markdown("- Be aware of the signs and symptoms of diabetes and seek medical advice if concerned.")
            st.markdown("- Monitor blood sugar levels as advised by healthcare professionals.")

        elif 40 <= age <= 64:
            st.markdown("## Diabetes for Middle Adulthood (Ages 40-64):")
            st.markdown("- Get screened for diabetes during routine health check-ups.")
            st.markdown("- Follow a diabetic-friendly diet and monitor carbohydrate intake.")
            st.markdown("- Stay physically active to improve blood sugar control.")

        else:
            st.markdown("## Diabetes for Older Adulthood (Ages 65+):")
            st.markdown("- Manage diabetes medications carefully, as older adults may be more susceptible to side effects.")
            st.markdown("- Monitor blood sugar levels regularly, especially if there are changes in medication or lifestyle.")
            st.markdown("- Maintain a healthy lifestyle with a balanced diet and regular exercise.")
    else:
        if age <= 18:
            st.markdown("## Prevention of Diabetes for Childhood and Adolescence (Ages 0-18):")
            st.markdown("- Encourage a balanced diet with moderate portions of carbohydrates, proteins, and healthy fats.")
            st.markdown("- Promote regular physical activity to maintain a healthy weight and improve insulin sensitivity.")
            st.markdown("- Limit sugary snacks and beverages.")
            st.markdown("- Monitor blood sugar levels if there's a family history of diabetes.")

        elif 19 <= age <= 39:
            st.markdown("## Prevention of Diabetes for Young Adulthood (Ages 19-39):")
            st.markdown("- Maintain a healthy weight through portion control and regular exercise.")
            st.markdown("- Consume a diet rich in fiber, whole grains, fruits, and vegetables to regulate blood sugar levels.")
            st.markdown("- Limit processed foods and sugary drinks.")
            st.markdown("- Get screened for diabetes if there are risk factors present, such as obesity or a sedentary lifestyle.")

        elif 40 <= age <= 64:
            st.markdown("## Prevention of Diabetes for Middle Adulthood (Ages 40-64):")
            st.markdown("- Manage weight through portion control, mindful eating, and regular physical activity.")
            st.markdown("- Monitor blood sugar levels regularly, especially if there's a family history of diabetes or other risk factors.")
            st.markdown("- Follow a diabetic-friendly diet, emphasizing complex carbohydrates, lean proteins, and healthy fats.")
            st.markdown("- Get regular medical check-ups to detect early signs of diabetes and manage blood sugar levels effectively.")

        else:
            st.markdown("## Prevention of Diabetes for Older Adulthood (Ages 65+):")
            st.markdown("- Stay physically active with activities like walking, swimming, or gardening.")
            st.markdown("- Monitor blood sugar levels regularly and adjust medication as needed under medical supervision.")
            st.markdown("- Follow a balanced diet tailored to individual nutritional needs and diabetes management goals.")


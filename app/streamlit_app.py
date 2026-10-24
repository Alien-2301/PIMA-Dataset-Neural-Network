import  streamlit as st
from    tensorflow import keras
import  time
import  pandas as pd
import  json
from    pathlib import Path

from preprocessing import prep

import numpy as np


st.set_page_config(
    page_title = "Diabetes Prediction Dataset",
    layout = "wide",
    initial_sidebar_state="expanded",
    menu_items = {
        "About" : (
            "**Diabetes Risk Predictor**: a neural-network classifier trained on the "
            "Pima Indians Diabetes dataset (768 patients).\n\n"
            "Built by San Shwe Htet for CM3015 Machine Learning.\n\n"
            "[GitHub repo](https://github.com/YOUR-USERNAME/diabetes-risk-prediction)\n\n"
            "*Educational project, not medical advice.*"
        ),
        "Get help": None,
        "Report a bug": "https://github.com/YOUR-USERNAME/diabetes-risk-prediction/issues",
    }
)

APP_DIR = Path(__file__).resolve().parent

MODEL_PATH = APP_DIR / "model.keras"
PREP_PATH = APP_DIR / "preprocessing.json"
PRED_PATH = APP_DIR / "test_prediction.csv"
CV_PATH = APP_DIR / "model_library.csv"


@st.cache_resource
def get_model():
    print("Loading model...")
    return keras.models.load_model(MODEL_PATH)


st.title("Diabetes Risk Predictor using Neural Networks")
st.caption("Educational project, not medical advice.")


model = get_model()

st.dataframe(pd.read_csv(CV_PATH))
# st.dataframe(pd.read_csv(PRED_PATH))
with open(PREP_PATH, "r") as file:
    prep_data = json.load(file)

# Form
with st.form("patient_form"):
    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0, max_value=20, value=3, step=1
    )

    glucose = st.number_input(
        "Glucose (mg/dL)",
        min_value=0, max_value=200, value=117, step=1
    )

    blood_pressure = st.number_input(
        "Blood pressure (mm Hg)",
        min_value=0, max_value=130, value=72, step=1
    )

    skin_thickness = st.number_input(
        "Skin thickness (mm)",
        min_value=0, max_value=100, value=29, step=1
    )

    insulin = st.number_input(
        "Insulin (μU/mL)",
        min_value=0, max_value=900, value=125, step=1
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0, max_value=70.0, value=32.4, step=0.1
    )

    dpf = st.number_input(
        "Diabetes pedigree function",
        min_value=0.0, max_value=2.5, value=0.38, step=0.01, format="%.3f"
    )

    age = st.number_input(
        "Age (years)",
        min_value=18, max_value=100, value=29, step=1
    )

    submitted = st.form_submit_button("Predict")

if submitted:
    st.table({
        "Variable": [
            "Pregnancies",
            "Glucose (mg/dL)",
            "Blood pressure (mm Hg)",
            "Skin thickness (mm)",
            "Insulin (μU/mL)",
            "BMI",
            "Diabetes pedigree function",
            "Age (years)"
        ],
        "Value": [
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            dpf,
            age
        ]
    })

    # double bracket for (1, 8) instead of (8,)
    row = np.array([[pregnancies, glucose, 
                    blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prepped = prep(row, prep_data)

    # single number (1,1) + stops progress bar from fillingterminal
    probability = model.predict(prepped, verbose=0)[0][0] 

    st.metric("Diabetes Probability: ", f"{probability:.1%}")

    

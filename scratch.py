import streamlit as st
import datetime as dt
from tensorflow import keras
import time


measuring = True
model = "app/model.keras"

if measuring is True:
    start_time = time.perf_counter()
    st.write("loading model")
    model = keras.models.load_model(model)
    measuring = False
    end_time = time.perf_counter()
else: 
    model = keras.models.load_model(model)

st.write(model)
st.write(f"Loaded in {end_time - start_time:.4f} seconds")

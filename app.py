import streamlit as st
import pandas as pd

st.title("Road Crash Prediction Dashboard")

weather = st.selectbox(
"Weather Condition",
["CLEAR","RAIN","SNOW","FOG"]
)

lighting = st.selectbox(
"Lighting Condition",
["DAYLIGHT","DARKNESS"]
)

vehicles = st.slider("Number of Vehicles",1,5,2)

month = st.slider("Crash Month",1,12,6)

hour = st.slider("Crash Hour",0,23,12)

if st.button("Predict"):

    if vehicles > 2 or hour > 20:
        result = "REPORTED INJURY"
    else:
        result = "NO INDICATION OF INJURY"

    st.success("Prediction: " + result)

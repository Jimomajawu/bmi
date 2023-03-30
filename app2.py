import streamlit as st
from PIL import Image

st.title("BMI Calculator App")

W = st.number_input("What is your weight in KG")
H= st.number_input("What is your height in metres")

def cal_bmi (W, H):
    bmi = round(W/(H**2),1)
    if bmi >= 30:
        return f' your bmi score is {bmi} and you are obese'
        

    elif bmi >=25:
        return f' your bmi score is {bmi} and you are overweight'
        
    elif bmi >=18.5:
        return f' your bmi score is {bmi} and you are healthyweight'
        
    else:
        return f' your bmi score is {bmi} and you are underweight'
    
if st.button("Calculate BMI"):
    st.write(cal_bmi(W, H))
        




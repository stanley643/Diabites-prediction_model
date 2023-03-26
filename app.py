
# create a streamlit app that will take input for the model in te hackathon.ipynb file
# and display the output

import streamlit as st
import pandas as pd
import numpy as np
import pickle

#load the model from the pickle file
model = pickle.load(open('','rb'))


# create a function that will take the inputs from the user
def predict_default(Pregnancies,Glucose,BloodPressure,SkinThickness,Isulin,BMI,DiabetesPedigreeFunction,Age):
    
    

    

 
    # Making predictions 
    prediction = model.predict( [Pregnancies,Glucose,BloodPressure,SkinThickness,Isulin,BMI,DiabetesPedigreeFunction,Age])

    # set prediction whole number integer
    prediction = int(prediction)

    return prediction

# main function
def main():
    st.title('''DIABITES PREDICTION MODEL''')
    Pregnancies = st.number_input('Input number of pregnancies')
    Glucose =  st.number_input('Glucose Level')
    BloodPressure = st.number_input('Blood Pressure')
    SkinThickness = st.number_input('Skin Thickness')
    Isulin =  st.number_input('Isulin')
    BMI = st.number_input('BMI')
    DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction')
    Age = st.number_input('Input your age')
    if button:
        prediction = predict_default(Pregnancies,Glucose,BloodPressure,SkinThickness,Isulin,BMI,DiabetesPedigreeFunction,Age)
        st.success('Return of 1 means YES and return of 0 means NO:{}'.format(prediction))

if __name__ == '__main__':
    main()

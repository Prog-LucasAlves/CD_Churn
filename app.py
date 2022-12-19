import pandas as pd
import streamlit as st

st.write("""
        Previsão de Churn\n
        App que utiliza Machine Learnig para prever Churn de clintes.\n
        Fonte: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
        """)

st.sidebar.text('Selecione os Dados dos Cliente:')

def getInfoData():
    SeniorCitizen = st.sidebar.slider('Idoso(a)',0, 0, 1)
    
    user_data = {
        'idoso':SeniorCitizen
    }
    
    features = pd.Dataframe(user_data, index=0)
    
    return features

userInputData = getInfoData()

info = st.bar_chart(userInputData)
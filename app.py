import pandas as pd
import streamlit as st

st.write("""
        Previsão de Churn\n
        App que utiliza Machine Learnig para prever Churn de clintes.\n
        Fonte: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
        """)

st.sidebar.text('Selecione os Dados dos Cliente:')

def getInfoData():
    SeniorCitizen = st.sidebar.slider(f'Idoso(a) 0->Não | 1->Sim',0, 0, 1)
    
    user_data = {
        'idoso':SeniorCitizen
    }
    
    features = pd.DataFrame(user_data, index=0)
    
    return features

userInputData = getInfoData()

info = st.bar_chart(userInputData)
import pandas as pd
import streamlit as st

st.write("""
        Previsão de Churn\n
        App que utiliza Machine Learnig para prever Churn de clintes.\n
        Fonte: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
        """)

st.sidebar.text('Selecione os Dados dos Cliente:')

st.write("-----------------------------------------")

st.subheader('Informações dos Dados')

def getInfoData():
    SeniorCitizen = st.sidebar.expander("Idoso(a)")
    nSeniorCitizen = SeniorCitizen.button("Não")
    ySeniorCitizen = SeniorCitizen.button("Sim")
    
    st.sidebar.write(nSeniorCitizen)
    st.sidebar.write(ySeniorCitizen)
    
    if nSeniorCitizen is True:
        a = 0
        
        st.write(a)
    
    else:
        a = 1
    
    user_data = {
        'idoso':a,

    }
    
    features = pd.DataFrame(user_data, index=[0])
    
    return features

userInputData = getInfoData()

grafico = st.bar_chart(userInputData)
st.subheader('Dados Do Cliente:')
st.write(userInputData)
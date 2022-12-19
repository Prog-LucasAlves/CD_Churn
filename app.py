import streamlit as st

st.write("""
        Previsão de Churn\n
        App que utiliza Machine Learnig para prever Churn de clintes.\n
        Fonte: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
        """)

st.sidebar.text('Selecione os Dados dos Cliente:')

def getInfoData():
    SeniorCitizen = st.sidebar.button('Idoso(a)', 'Sim', 'Não')
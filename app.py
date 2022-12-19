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
    SeniorCitizen = st.sidebar.slider(f'Idoso(a) 0->Não | 1->Sim',0, 0, 1)
    Partner = st.sidebar.slider('Tem Parceiro(a) 0->Não | 1-Sim',0 ,0 ,1)
    cm_expander = st.sidebar.beta_expander("Application Cat - 1 ",expanded=True)
    sa_button_clicked = cm_expander.button("Application - 1")
    sr_button_clicked = cm_expander.button("Application - 2")
    sb_button_clicked = cm_expander.button("Application - 3")
    
    user_data = {
        'idoso':SeniorCitizen,
        'parceiro':Partner
    }
    
    features = pd.DataFrame(user_data, index=[0])
    
    return features

userInputData = getInfoData()

grafico = st.bar_chart(userInputData)
st.subheader('Dados Do Cliente:')
st.write(userInputData)
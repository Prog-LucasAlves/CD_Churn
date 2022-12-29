import pandas as pd
import streamlit as st
import time



@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")


st.write("""
        Previsão de Churn\n
        App que utiliza Machine Learnig para prever Churn de clintes.\n
        Fonte: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
        """)

st.sidebar.text('Selecione os Dados dos Cliente:')

st.write("-----------------------------------------")


st.sidebar.header('Informações dos Clientes:')
a = 0
SeniorCitizen = st.sidebar.selectbox('Cliente e Idoso(a):',
                                    ('Não', 'Sim'))
st.write('You selected:', SeniorCitizen)


if SeniorCitizen == 'Não':
    a = 0
if SeniorCitizen == 'Sim':
    a = 1
        

user_data = {
        'Idoso': a,
    }

features = pd.DataFrame(user_data, index=[0])

userInputData = features                 

st.subheader('Dados Do Cliente:')
st.write(features)



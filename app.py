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
st.sidebar.write('You selected:', SeniorCitizen)

if SeniorCitizen == 'Não':
    a = 0
if SeniorCitizen == 'Sim':
    a = 1

b = 0
Dependents = st.sidebar.selectbox('Cliente tem Dependente:',
                                 ('Não', 'Sim'))
st.sidebar.write('You selected:', Dependents)

if Dependents == 'Não':
    b = 0
if Dependents == 'Sim':
    b = 1

tenure = st.sidebar.number_input('Quantos Meses o Cliente esta na Empresa:', step=0, max_value=75)
st.sidebar.write('You selected:', tenure)

user_data = {
    'Idoso': a,
    'Tem Dependente': b,
    'Meses como Cliente': tenure
            }

features = pd.DataFrame(user_data, index=[0])

userInputData = features         

st.subheader('Dados Do Cliente:')
st.write(features)

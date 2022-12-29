import pandas as pd
import streamlit as st
import time

'''
st.write("""
        Previsão de Churn\n
        App que utiliza Machine Learnig para prever Churn de clintes.\n
        Fonte: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
        """)

st.sidebar.text('Selecione os Dados dos Cliente:')

st.write("-----------------------------------------")


st.sidebar.header('Informações dos Clientes:')
a = 0
st.sidebar.text('Idoso(a):')
nSeniorCitizen = st.sidebar.button('Não', key=1)
ySeniorCitizen = st.sidebar.button('Sim', key=2)
    
if nSeniorCitizen is True:
    a = 0
if ySeniorCitizen is True:
    a = 1
        
b = 0
st.sidebar.text('Idoso(a):')
nDependents = st.sidebar.button('Não', key=3)
yDependents = st.sidebar.button('Sim', key=4)

if nDependents is True:
    b = 0
if yDependents is True:
    b = 1

user_data = {
        'Idoso': a,
        'Tem Dependente': b
    }

features = pd.DataFrame(user_data, index=[0])

userInputData = features                 

st.subheader('Dados Do Cliente:')
st.write(features)
'''

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return {"output": a * b}  # 👈 Mutable object

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)

res["output"] = "result was manually mutated"  # 👈 Mutated cached value

st.write("Mutated result:", res)
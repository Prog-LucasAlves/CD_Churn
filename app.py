import pandas as pd
import streamlit as st
from streamlit_disqus import st_disqus

st_disqus("streamlit-disqus-demo")

st.write("""
        Previsão de Churn\n
        App que utiliza Machine Learnig para prever Churn de clintes.\n
        Fonte: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
        """)

st.sidebar.text('Selecione os Dados dos Cliente:')

st.write("-----------------------------------------")


a = 0
ExpanderP = st.sidebar.expander("Informações", expanded=True)
ExpanderP.text('Idoso(a):')
nSeniorCitizen = ExpanderP.button("Não", key=1)
ySeniorCitizen = ExpanderP.button("Sim", key=2)

if nSeniorCitizen is True:
    a = 0
if ySeniorCitizen is True:
    a = 1

ExpanderZ = st.sidebar.expander("Informações", expanded=True)
b = 0
ExpanderZ.text('Tem Dependente:')
nDependents = ExpanderZ.button("Não", key=3)
yDependents = ExpanderZ.button("Sim", key=4)

if nDependents is True:
    b = 0
if yDependents is True:
    b = 1
    
st.write(a)
st.write(b)

user_data = {
        'Idoso': a,
        'Tem Dependente': b,
    }

features = pd.DataFrame(user_data, index=[0])



userInputData = features                   

st.subheader('Dados Do Cliente:')
st.write(userInputData)

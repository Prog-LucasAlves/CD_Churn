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


def getInfoData():

    a = 0
    SeniorCitizen = st.sidebar.expander("Idoso(a):")
    nSeniorCitizen = SeniorCitizen.button("Não")
    ySeniorCitizen = SeniorCitizen.button("Sim")

    if nSeniorCitizen is True:
        a = 0
    if ySeniorCitizen is True:
        a = 1

    b = 0
    Dependents = st.sidebar.expander("Tem Dependente:")
    #nDependents = Dependents.button("Não")
    #yDependents = Dependents.button("Sim")

    #if nDependents is True:
        #b = 0
    #if yDependents is True:
       # b = 1

    user_data = {
        'Idoso': a,
        'Tem Dependente': b,
    }

    features = pd.DataFrame(user_data, index=[0])
    return features


userInputData = getInfoData()                    

st.subheader('Dados Do Cliente:')
st.write(userInputData)

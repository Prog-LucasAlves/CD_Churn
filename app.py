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
    ExpanderP = st.sidebar.expander("Informações", expanded=True)
    ExpanderP.text('Idoso(a):')
    nSeniorCitizen = ExpanderP.button("Não")
    ySeniorCitizen = ExpanderP.button("Sim")
    ExpanderP.text('Tem Dependente:')
    nDependents = ExpanderP.button("l")
    yDependents = ExpanderP.button("S")

    user_data = {
        'Idoso': a,
        'Tem Dependente': b,
    }

    features = pd.DataFrame(user_data, index=[0])
    return features


userInputData = getInfoData()                    

st.subheader('Dados Do Cliente:')
st.write(userInputData)

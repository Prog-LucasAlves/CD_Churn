import pandas as pd
import streamlit as st


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

tenure = st.sidebar.number_input('Quantos Meses o Cliente esta na Empresa:',
                                 step=0,
                                 max_value=75)
st.sidebar.write('You selected:', tenure)

c = 0
InternetService = st.sidebar.selectbox('Possui Serviço de Internet:',
                                       ('Não', 'DSL'))
st.sidebar.write('You Selected:', InternetService)

if InternetService == 'Não':
    c = 0
elif InternetService == 'DSL':
    c = 1
else:
    c = 0

d = 0
Contract = st.sidebar.selectbox('Duração do Contrato:',
                                ('Mensal', 'Anual', 'Bienal'))
st.sidebar.write('You Selected:', Contract)

if Contract == 'Mensal':
    d = 0
elif Contract == 'Anual':
    d = 1
else:
    d = 2

e = 0
PaperlessBilling = st.sidebar.selectbox('Fatura é via papel:',
                                        ('Não', 'Sim'))
st.sidebar.write('You Selected:', PaperlessBilling)

if PaperlessBilling == 'Não':
    e = 0
else:
    e = 1

f = 0
PaymentMethod = st.sidebar.selectbox('Meio de Pagamento:',
                                     ('Fatura via Correios', 
                                      'Fatura via E-mail',
                                      'Transferência Bancária', 
                                      'Cartão de Credito'))
st.sidebar.write('You selected:', PaymentMethod)

if PaymentMethod == 'Fatura via Correios':
    f = 0
elif PaymentMethod == 'Fatura via E-mail':
    f = 1
elif PaymentMethod == 'Transferência Bancária':
    f = 2
else:
    f = 3

MonthlyCharges = st.sidebar.number_input('Valor da Mensalidade:')
st.sidebar.write('You selected:', MonthlyCharges)

TotalCharges = MonthlyCharges * tenure

'''
g = 0
if InternetService == 'Sim':
    g = 0
    OnlineSecurity = st.sidebar.selectbox('Possui Serviço de Segurança OnLine:',
                                          ('Sim', 'Não'))
    st.sidebar.write('You selected:', OnlineSecurity)
    
    if OnlineSecurity == 'Não':
        g = 0
    else:
        g = 1
'''

user_info = {
    'Idoso(a)': SeniorCitizen,
    'Tem Dependente': Dependents,
    'Meses como Cliente': tenure,
    'Possui Serviço de Internet': InternetService,
    'Duração do Contrato': Contract,
    'Fatura é via papel': PaperlessBilling,
    'Meio de Pagamento': PaymentMethod,
    'Valor da Mensalidade': round(MonthlyCharges, 2),
    'Valor Total dos Serviços desde o Inicio': round(TotalCharges, 2)
}
features_info = pd.DataFrame(user_info, index=[0])
features_info = features_info.T

user_data = {
    'Idoso(a)': a,
    'Tem Dependente': b,
    'Meses como Cliente': tenure,
    'Possui Serviço de Internet': c,
    'Duração do Contrato': d,
    'Fatura é via papel': e,
    'Meio de Pagamento': f,
    'Valor da Mensalidade': round(MonthlyCharges, 2),
    'Valor Total dos Serviços desde o Inicio': round(TotalCharges, 2)
}
features_data = pd.DataFrame(user_data, index=[0])
features_data = features_data.T

st.subheader('👪 Dados Do Cliente:')
st.write(features_info)

st.write("-----------------------------------------")

st.subheader('⚙️ Dados Do Cliente Para Modelo:')
st.write(features_data)
st.write(features_data.dtypes)

st.write("-----------------------------------------")

# Previsão de churn com aprendizado de máquina

## Referência

- [Fonte](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## Objetivo

- Classificar se um cliente vai **deixar(sair) a empresa - Cancelar os serviços**.

## Descrição - Problema de negocio

- A empresa Telco.com quer avaliar com base nos dados dos seus clientes se algum cliente vai cancelar os serviços da empresa.

## Definições

- Coluna 'Churn' Codificação -> | 1 para Yes(Saiu da Empresa) - 0 para No(Não Saiu da Empresa)
- Coluna 'Gender' Sexo do Cliente Codificação -> | 1 para Female(Feminino) - 0 para Male(Masculino)
- Para as colunas 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling' Codificação | 1 para Yes - 0 para No
- Coluna 'Contract' Codificação | 2 para Month-to-month - 1 para Two year - 0 One year
- Coluna 'InternetService' | 2 para Fiber optic - 1 para DSL - 0 para No
- Coluna 'PaymentMethod' | 3 para Credit card (automatic) - 2 para Bank transfer (automatic) - 1 para Electronic check - 0 para Mailed check

## Resultado

| Modelo | Dataset | Resultado |
| ------ | ------- | --------- |

## Planejamento

- [ ] - Analisar os dados (Limpeza e Transformação dos dados)
- [ ] - Previssão de churn
- [ ] - Deploy do Modelo

## App(Streamlit)

- [APP](https://cd-churn.streamlit.app/)

![progress](https://progress-bar.dev/10/?title=completed "progresso")

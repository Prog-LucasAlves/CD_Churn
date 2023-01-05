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

| Modelo | Dataset | Coluna(s) Eliminadas | Resultado(Metrica: 'f1') | Acurácia |
| ------ | ------- | -------------------- |------------------------- | -------- |
| Regressao Logistica | Data_Transformedv1.0.csv | Nenhuma | 58.80 | 81.54% |
| Regressao Logistica | Data_Transformedv2.0.csv | gender | 58.79 | 81.68% |
| Regressao Logistica | Data_Transformedv3.0.csv | gender - Partner | 58.84 | 81.68% |
| Regressao Logistica | Data_Transformedv4.0.csv | gender - Partner - TotalCharges | 58.48 | 81.47% |
| Regressao Logistica | Data_Transformedv5.0.csv | gender - Partner - TotalCharges - MonthlyCharges | 58.48 | 81.47% |
| Regressao Logistica | Data_Transformedv6.0.csv | 20 Mellhores features(f_classif)v1 | 58.46 | 81.61% |
| Regressao Logistica | Data_Transformedv7.0.csv | 18 Mellhores features(f_classif)v1 | 58.22 | 81.61% |
| Regressao Logistica | Data_Transformedv8.0.csv | 20 Mellhores features(f_classif)v2 | 58.46 | 81.61% |
| Regressao Logistica | Data_Transformedv9.0.csv | 18 Mellhores features(f_classif)v2 | 58.28 | 81.47% |
| Regressao Logistica | Data_Transformedv10.0.csv | 20 Mellhores features(f_classif)v3 | 57.06 | 81.83% |
| Regressao Logistica | Data_Transformedv11.0.csv | 18 Mellhores features(f_classif)v3 | 56.62 | 81.76% |
| Regressao Logistica | Data_Transformedv12.0.csv | 15 Mellhores features(f_classif)v1 | 56.18 | 81.68% |
| Regressao Logistica | Data_Transformedv13.0.csv | 10 Mellhores features(f_classif)v1 | 53.82 | 80.62% |
| Regressao Logistica | Data_Transformedv14.0.csv | gender - PhoneService - MultipleLines_No phone service - MultipleLines_Yes | 58.52 | 81.47% |
| Regressao Logistica | Data_Transformedv15.0.csv | gender - PhoneService | 58.83 | 81.47% |
| Regressao Logistica | Data_Transformedv16.0.csv | gender - Partner | 58.82 | 81.68% |
| Regressao Logistica | Data_Transformedv17.0.csv | 10 Mellhores features(f_classif)v2 | 56.95 | 80.26% |
| Regressao Logistica | Data_Transformedv18.0.csv | 15 Mellhores features(f_classif)v2 | 58.24 | 80.76% |
| Regressao Logistica | Data_Transformedv19.0.csv | 18 Mellhores features(f_classif)v4 | 58.59 | 81.47% |
| Regressao Logistica | Data_Transformedv20.0.csv | 20 Mellhores features(f_classif)v4 | 58.20 | 81.97% |
| Regressao Logistica | Data_Transformedv21.0.csv | 20 Mellhores features(f_classif)v5 | 58.74 | 81.40% |

## Planejamento

- [x] - Analisar os dados (Limpeza e Transformação dos dados)
- [x] - Previssão de churn
- [ ] - Deploy do Modelo

## App(Streamlit)

- [APP](https://cd-churn.streamlit.app/)

![progress](https://progress-bar.dev/60/?title=completed "progresso")
[![Linter](https://github.com/Prog-LucasAlves/CD_Churn/actions/workflows/Linter.yml/badge.svg)](https://github.com/Prog-LucasAlves/CD_Churn/actions/workflows/Linter.yml)

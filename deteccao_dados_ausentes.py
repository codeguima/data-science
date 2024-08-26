import pandas as pd

## Carregar Dataframes de Serviços (Services)
df_customers = pd.read_csv('./datasets/churn_customers.csv')
df_services = pd.read_csv('./datasets/churn_services.csv')
df_contracts = pd.read_csv('./datasets/churn_contracts.csv')

#transformar coluna totalcharges de string para float
df_contracts.TotalCharges = pd.to_numeric(df_contracts.TotalCharges, errors='coerce')

#rename usando Lista - Modificar todos os nomes de colunas
df_customers.columns = ['IDCliente', 'Genero', 'Mais65anos', 'TemParceiro', 'TemDependentes']

#renomear colunas
df_services.rename(columns={'customerID': 'IDCliente'}, inplace=True)

#UNIFICAR DE CUSTOMERS, SERVICES E CONTRACTS, CRIANDO UM TERCEIRO DATAFRAME

df_temp = df_customers.merge(df_services, on=['IDCliente'])

#UNIFICAR df_temp COM CONTRACTS, USANDO COLUNAS DE JUNÇÃO COM NOMES DISTINTOS

df_churn_temp = df_temp.merge(df_contracts, left_on='IDCliente', right_on=['customerID'])

#print(df_churn_temp.info())

#UNIFICAR OS TRÊS DATAFRAMES AO MESMO TEMPO, COM COLUNAS COM NOMES DIFERENTES
df_churn = df_customers.merge(df_services, on=['IDCliente']).merge(df_contracts, left_on=['IDCliente'], right_on=['customerID'])

#retira a coluna do dataframe
df_churn.drop(['customerID'], axis=1, inplace=True)
#----------------------------------------------------------------------------------------------------#

#DETECÇÃO DE DADOS AUSENTES

# detectar valores ausentes
#print(df_churn.isna().sum())

# detectar valores ausentes em uma coluna
#print(df_churn.TotalCharges.isna().sum())

#quantas linhas tem pelo menos 1 coluna com o valor ausente
#print(df_churn[df_churn.isna().any(axis=1)])

#quantas colunas tem pelo menos 1 valor ausente
print(df_churn.isna().any(axis=0).sum())

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

#REMOÇÃO DE VALORES AUSENTES

#remover de forma direta e especifica a coluna que possui valores ausentes
#print(df_churn.drop(columns=['TotalCharges'], axis=1))

#remover colunas com valores ausentes
#df_churn.dropna(axis=1)

#remover colunas com todos os valores são ausentes
#print(df_churn.dropna(axis=1, how='all'))

#remover linhas com os valores são ausentes
#print(df_churn.dropna(axis=0))

#preencher toto os valores ausentes com 0
#print(df_churn.fillna(0))

#preencher os valores padrão conforme a coluna
#print(df_churn.fillna(value={'TotalCharges': 0, 'Genero': 'Não Declarado'}))

#preencher todos os valores ausentes de uma coluna com a média
media_TotalCharges = df_churn.TotalCharges.mean()

print(media_TotalCharges)

#inputar a media no dataframe
print(df_churn.fillna(value={'TotalCharges': media_TotalCharges }))
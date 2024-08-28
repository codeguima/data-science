import pandas as pd

## Carregar Dataframes de Serviços (Services)
df_customers = pd.read_csv('./datasets/churn_customers.csv')
df_services = pd.read_csv('./datasets/churn_services.csv')
df_contracts = pd.read_csv('./datasets/churn_contracts.csv')

##imprmir dataframe
#print(df_customers.info())

#verificar tamanho do dataframe
#print(len(df_customers))

#rename usando Lista - Modificar todos os nomes de colunas
df_customers.columns = ['IDCliente', 'Genero', 'Mais65anos', 'TemParceiro', 'TemDependentes']

#renomear colunas
df_services.rename(columns={'customerID': 'IDCliente'}, inplace=True)

#print(df_services.info())

#UNIFICAR DE CUSTOMERS, SERVICES E CONTRACTS, CRIANDO UM TERCEIRO DATAFRAME

df_temp = df_customers.merge(df_services, on=['IDCliente'])

#print(df_temp.info())

#MOSTRAR AS 5 PRIMEIRAS LINHAS
#print(df_temp.head(5))


#UNIFICAR df_temp COM CONTRACTS, USANDO COLUNAS DE JUNÇÃO COM NOMES DISTINTOS

df_churn_temp = df_temp.merge(df_contracts, left_on='IDCliente', right_on=['customerID'])

print(df_churn_temp.info())

#UNIFICAR OS TRÊS DATAFRAMES AO MESMO TEMPO, COM COLUNAS COM NOMES DIFERENTES
df_churn = df_customers.merge(df_services, on=['IDCliente']).merge(df_contracts, left_on=['IDCliente'], right_on=['customerID'])


#retira a coluna do dataframe
df_churn.drop(['customerID'], axis=1, inplace=True)

print(df_churn.info())
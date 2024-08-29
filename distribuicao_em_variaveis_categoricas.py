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

#print(df_churn_temp.info())

#UNIFICAR OS TRÊS DATAFRAMES AO MESMO TEMPO, COM COLUNAS COM NOMES DIFERENTES
df_churn = df_customers.merge(df_services, on=['IDCliente']).merge(df_contracts, left_on=['IDCliente'], right_on=['customerID'])


#retira a coluna do dataframe
#df_churn.drop(['customerID'], axis=1, inplace=True)

#print(df_churn.info())

#-----------------------------------------------------------------------------------------------------------------/

#ANÁLISE UNIVARIADA
#HIPOTESES:
# -A faixa etária  do cliente tem uma forte associação com o churn
# -Um Cliente com menos de 6 meses de contrato é mais propenso ao churn
# -Cliente com contrato mensal é mais propenso ao Churn

#como contar pessoas que abondonaram um serviço
#Contar clientes usando a variavel Churn como referencias
#print(df_churn.Churn.value_counts())

#quais os valores unicos desta variavel
#print(df_churn.Churn.unique())

#como é a distribuição de clientes percentualmente falando  que abandonaram ou não ou serviço
#print(df_churn.Churn.value_counts(normalize=True))

#Plot distribuição Churn (Quantidade)
df_churn.Churn.value_counts().plot.bar()

#outra opção de grafico

ax = df_churn.Churn.value_counts().plot.bar()

ax.bar_label(ax.containers[0])
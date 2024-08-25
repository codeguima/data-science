import pandas as pd

##criar  dataFrames com based nos datasets

## Carregar Dataframes de clientes (customers)
df_customers = pd.read_csv('./datasets/churn_customers.csv')


## mostrar 5 primeiros registros do Dataframe
#print(df_customers.head(5))


## mostrar 5 ultimos registros do Dataframe
#print(df_customers.tail(5))

## mostar a estrutura / schema do dataFrame
#print(df_customers.info())

## Carregar Dataframes de Serviços (Services)
#df_services = pd.read_csv('./datasets/churn_services.csv')

## mostrar 5 primeiros registros do Dataframe
#print(df_services.head(5))


## mostrar 5 ultimos registros do Dataframe
#print(df_services.tail(5))

## mostar a estrutura / schema do dataFrame
#print(df_services.info())

## Carregar Dataframes de Serviços (Services)
df_contracts = pd.read_csv('./datasets/churn_contracts.csv')

## mostrar 5 primeiros registros do Dataframe
#print(df_contracts.head(5))


## mostrar 5 ultimos registros do Dataframe
#print(df_contracts.tail(5))

## mostar a estrutura / schema do dataFrame
print(df_contracts.info())
import pandas as pd

##criar  dataFrames com based nos datasets

## Carregar Dataframes de clientes (customers)
df_customers = pd.read_csv('./datasets/churn_customers.csv')


## mostrar 5 primeiros registros do Dataframe
print(df_customers.head(5))


## mostrar 5 ultimos registros do Dataframe
print(df_customers.tail(5))

## mostar a estrutura / schema do dataFrame
print(df_customers.info())




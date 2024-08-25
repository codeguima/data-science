import pandas as pd

## Carregar Dataframes de Serviços (Services)
df_customers = pd.read_csv('./datasets/churn_customers.csv')
##imprmir dataframe
#print(df_customers.info())

#verificar tamanho do dataframe
print(len(df_customers))

#UNIFICAR DE CUSTOMERS, SERVICES E CONTRACTS, CRIANDO UM TERCEIRO DATAFRAME


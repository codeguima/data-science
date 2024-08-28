import pandas as pd

## Carregar Dataframes de Serviços (Services)
df_customers = pd.read_csv('./datasets/churn_customers.csv')
##imprmir dataframe
#print(df_customers.info())

## renomear colunas do dataframe

#print(df_customers.rename(columns={'SeniorCitizen':'Above65yo'}))


## criar um dataframe novo com base nas colunas renomeadas

#df_customers_renamed = df_customers.rename(columns={'SeniorCitizen':'Above65yo'})

#print(df_customers_renamed.info())

#aplicar o resultado do rename no própio DataFrame
#df_customers.rename(columns={'SeniorCitizen':'Above65yo'}, inplace=True)

#rename usando Lista - Modificar todos os nomes de colunas
df_customers.columns = ['IDCliente', 'Genero', 'Mais65anos', 'TemParceiro', 'TemDependentes']

print(df_customers.info())



import pandas as pd

## Carregar Dataframes de Serviços (Services)
df_contracts = pd.read_csv('./datasets/churn_contracts.csv')

#transformar coluna totalcharges de string para float
df_contracts.TotalCharges = pd.to_numeric(df_contracts.TotalCharges, errors='coerce')

print(df_contracts.info())

#após a transformação da coluna TotalCharges do dataframe Contracts, a coluna passou a ter 11 valorers ausentes(missing values)
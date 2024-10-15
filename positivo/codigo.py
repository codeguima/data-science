import pandas as pd
import numpy as np 

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('./datasets/SMSSpamCollection', sep='\t', header=None)
df.columns = ['target', 'text']

print(df)

df['target'] = df['target'].apply(lambda x: 1 if x == 'spam' else 0)

df.target.value_counts(normalize=True)

X = df['text']
y= df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

X_train_indices = X_train.index
X_test_indices = X_test.index

X_train_text = df['text'].iloc[X_train_indices]
X_test_text = df['text'].iloc[X_test_indices]

vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train_text)
X_test_tfidf = vectorizer.transform(X_test_text)

model = RandomForestClassifier()

model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)

y_pred

y_proba = model.predict_proba(X_test_tfidf)

y_proba

y_proba_1 = y_proba[:,1]

y_proba_1

df_count = y_test.count() + y_train.count()

# Histograma, considerando a parte de teste, com a saída das probabilidades da classe positiva (1), ex: é spam
pd.DataFrame(y_proba_1).hist(bins = 10)

# total da coluna / total de tudo
# mudar a escala da contagem

# Gerar o histograma e capturar os bins e as contagens
y_proba_count, bin_edges = np.histogram(y_proba_1, bins=10)

y_proba_count

y_proba_percentage = (y_proba_count / (y_proba_count.sum())) * 100

y_proba_percentage

df_results = pd.DataFrame({
  'y_proba_1': y_proba_1, # probabiliadde positiva
  'y_test': y_test
})

df_results_filtered = df_results[df_results['y_test'] == 1]

df_results_filtered['y_proba_1'].hist(bins=10)
# Quando a probabilidade é muito baixa, possivelmente o modelo errou
# No meio ele não acerta muito bem
# A maioria que a gente sabe que 


# Gerar o histograma e capturar os bins e as contagens
y_proba_1_filtered = df_results_filtered['y_proba_1']

y_proba_1_filtered_count, bin_edges = np.histogram(y_proba_1_filtered, bins=10)

y_proba_1_filtered_count

y_proba_filtered_percentage = (y_proba_1_filtered_count / (y_proba_1_filtered_count.sum())) * 100

y_proba_filtered_percentage

df_melt = pd.DataFrame({
  'filtered_proba': y_proba_filtered_percentage, # probabiliadde positiva
  'proba': y_proba_percentage
})

df_melt


# Definindo o tamanho do gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Definindo a largura das barras
bar_width = 0.35
index = range(len(df_melt))

# Plotando as barras lado a lado
ax.bar(index, df_melt['filtered_proba'], bar_width, label='População positiva')
ax.bar([i + bar_width for i in index], df_melt['proba'], bar_width, label='População geral')

# Adicionando os detalhes do gráfico
ax.set_xlabel('Probabilidades')
ax.set_ylabel('% da população')
ax.set_title('Gráfico de pontos de corte para classificação binária')

# Adicionando o eixo x em porcentagem
percentages = ['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%']
ax.set_yticklabels(percentages)

percentages = ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%']
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(percentages)
# ax.set_yticklabels(percentages)

# Exibindo o gráfico
ax.legend()
plt.tight_layout()
plt.show()
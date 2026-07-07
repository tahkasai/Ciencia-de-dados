import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('arquivo.csv')

plt.hist(df['Idade'].dropna(), bins=10) # dropna() se tiver um dado incompleto, ele ignora
plt.title('Distribuição de variavies')
plt.ylabel('Quantidade')
plt.xlabel('Idades')
plt.show()

# Salva o histograma como png
plt.savefig('Distribuição de dados/Histograma.png', dpi=300, bbox_inches='tight')
plt.close()
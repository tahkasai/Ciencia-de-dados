import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('arquivo.csv')

sns.set_theme(style='whitegrid')
ax = sns.boxplot(x=df['Idade'])

# Salva como png
plt.savefig('Boxplot/boxplot.png', dpi=300, bbox_inches='tight')
plt.close()
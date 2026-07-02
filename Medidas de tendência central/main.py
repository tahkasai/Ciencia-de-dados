import pandas as pd

df = pd.read_csv('arquivo.csv')

print("Idade média \n",df.Idade.mean()) 
print("Idade Mediana \n",df.Idade.median()) 
print("Idade Moda \n", df.Idade.mode().tolist())
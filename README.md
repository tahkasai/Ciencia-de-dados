# Estudo sobre Ciência de Dados
Esse repositório tem com objetivo colocar em prática os estudos referente a ciência de dados.

## O que são medidas de tendência central?
As medidas de tendência central ajudam a resumir um conjunto de dados em um único valor que representa o comportamento geral dos dados.

- Média: é o valor obtido somando todos os números e dividindo pela quantidade de valores.
- Mediana: é o valor central quando os dados são organizados em ordem.
- Moda: é o valor que aparece com mais frequência.

<!-- ## Como executar o projeto
1. Ative o ambiente virtual:
   ```bash
   source .venv/bin/activate
   ```
2. Execute o script:
   ```bash
   python "Medidas de tendência central/main.py"
   ``` -->

### Exemplo de código
```python
import pandas as pd

df = pd.read_csv('arquivo.csv')

print("Média:", df.Idade.mean())
print("Mediana:", df.Idade.median())
print("Moda:", df.Idade.mode().tolist())
```

## Distribuição de dados
> histograma: ferramenta para avaliar a distribuição dos dados. Ele consiste em um gráfico de barras vertical que apresentam distribuição de frequência dos dados.

Existem três tipos de distribuição, sendo elas:
* Simétrica, onde a medidas de tendencia tem valores iguais.
* Assimetrica à direita, onde: Moda -> Mediana -> Media
* Assimetrica à esquerda, onde: Media -> Mediana -> Moda. 

### Exemplo de código
```python
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
```
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

## Medidas separatrizes, dispersão e box-plot
As medidas separatrizes dividem um conjunto de dados em partes iguais e ajudam a entender a posição dos valores dentro da distribuição.

- Quartis: dividem os dados em 4 partes iguais.
   - $Q1$ deixa 25% dos dados abaixo dele.
   - $Q2$ é a mediana e deixa 50% dos dados abaixo dele.
   - $Q3$ deixa 75% dos dados abaixo dele.
- Quintis: dividem os dados em 5 partes iguais.
- Percentis: dividem os dados em 100 partes iguais.

Em dados assimétricos, a distribuição não é equilibrada em torno da média.
- Assimetria à direita: a cauda fica mais longa do lado dos valores altos.
- Assimetria à esquerda: a cauda fica mais longa do lado dos valores baixos.

Nesses casos, a mediana e os quartis costumam representar melhor o comportamento do conjunto do que a média.

### Dispersão de dados
A dispersão mostra o quanto os dados se espalham em relação ao valor central.

- Amplitude: diferença entre o maior e o menor valor.
- Variância: mede o quanto os dados se afastam da média.
- Desvio padrão: é a raiz quadrada da variância e mostra a dispersão na mesma unidade dos dados.
- Intervalo interquartil (IQR): $Q3 - Q1$.

O IQR é muito usado porque funciona bem em conjuntos assimétricos e também é a base para identificar outliers.

### O que é box-plot?
O box-plot é um gráfico que resume a distribuição dos dados usando mediana, quartis, dispersão e possíveis outliers.

Ele mostra:
- a caixa, que vai de $Q1$ a $Q3$;
- a linha central, que representa a mediana;
- os bigodes, que indicam a faixa dos valores não extremos;
- os pontos fora dos bigodes, que representam outliers.

### O que são outliers e como calcular
Outliers são valores muito distantes do restante do conjunto de dados. Eles podem indicar erro de medição, exceção real ou um comportamento diferente do padrão.

Um método comum para identificá-los usa o intervalo interquartil:

```text
IQR = Q3 - Q1
Limite inferior = Q1 - 1.5 * IQR
Limite superior = Q3 + 1.5 * IQR
```

Qualquer valor menor que o limite inferior ou maior que o limite superior é considerado outlier.

### Exemplo de código com box-plot
O exemplo abaixo usa o script da pasta [Boxplot](Boxplot/main.py) para gerar um box-plot da coluna `Idade` do arquivo `arquivo.csv`.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('arquivo.csv')

sns.set_theme(style='whitegrid')
ax = sns.boxplot(x=df['Idade'])

# Salva como png
plt.savefig('Boxplot/boxplot.png', dpi=300, bbox_inches='tight')
plt.close()
```

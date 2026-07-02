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


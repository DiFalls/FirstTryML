#1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.
def filtrar_impares(lista): # Função com objetivo de retornar apenas os números ímpares da lista fornecida.
    return [num for num in lista if num % 2 != 0] # Verifica, para cada número "num" na lista, se o resto da divisão por 2 é diferente de 0 (condição para ser ímpar).

#2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.
def e_primo(numero): # Função que verifica se um número é primo (números primos são maiores que 1 e divisíveis apenas por 1 e por ele mesmo.)
    
    if numero < 2:
        return False # Retorna False se o número for menor que 2, já que números menores que 2 não são primos.
    
    for i in range(2, int(numero**0.5) + 1): # Itera do número 2 até a raiz quadrada do número (inclusive).
        if numero % i == 0:
            return False # Se o número for divisível por qualquer valor dentro desse intervalo, ele não é primo.
    return True # Se nenhum divisor for encontrado, retorna True, indicando que o número é primo.

def filtrar_primos(lista): # Função que filtra os números primos em uma lista fornecida.
    return [num for num in lista if e_primo(num)] # Cria uma nova lista contendo apenas os números da lista original que são primos.

#3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
def diferenca_listas(lista1, lista2): # Define uma função chamada "diferenca_listas" que recebe duas listas como parâmetros: "lista1" e "lista2".
    
    return list(set(lista1).symmetric_difference(lista2)) # Converte ambas as listas em conjuntos utilizando a função "set()". 

#4.Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.
def segundo_maior(lista):
    lista_unica = list(set(lista)) # Remove duplicados
    lista_unica.sort() # Ordena em ordem crescente
    return lista_unica[-2] if len(lista_unica) > 1 else None # Retorna o segundo maior

#5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.
def ordenar_por_nome(lista_tuplas):
    # Define uma função chamada "ordenar_por_nome" que recebe uma lista de tuplas como parâmetro.
    # Cada tupla na lista deve conter, no mínimo, dois elementos, sendo o primeiro elemento (x[0]) o nome.

    return sorted(lista_tuplas, key=lambda x: x[0])  
    # A função "sorted()" é usada para ordenar a lista.
    # O argumento "key=lambda x: x[0]" especifica que a ordenação deve ser feita com base no primeiro elemento de cada tupla (que é o nome).
    # O "lambda x: x[0]" é uma função anônima que extrai o primeiro elemento da tupla para usá-lo como critério de ordenação.
    # O resultado será uma nova lista ordenada alfabeticamente pelos nomes.

#6. Observe os espaços sublinhados e complete o código.
import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")
for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                               transform=axs[row, col].transAxes,
                               ha='center', va='center', fontsize=18,
                               color='darkgrey')
fig.suptitle('plt.subplots()')

#7. Observe os espaços sublinhados e complete o código.
# Importando bibliotecas
import numpy as np  # Importa a biblioteca NumPy, usada para operações matemáticas e criação de arrays.
import matplotlib as mpl  # Importa o módulo principal do Matplotlib, utilizado para configurações mais gerais de gráficos.
import matplotlib.pyplot as plt  # Importa a interface Pyplot do Matplotlib, usada para criar gráficos de forma simples.

# Geração de dados para o gráfico
x = np.linspace(-2 * np.pi, 2 * np.pi, 100) # Cria um array "x" com 100 pontos igualmente espaçados no intervalo de -2π a 2π.
y = np.sin(x) # Calcula o seno para cada valor de "x" e armazena os resultados no array "y".

# Criação da figura e dos eixos
fig, ax = plt.subplots() # Cria uma figura (área do gráfico) e um conjunto de eixos (ax), onde o gráfico será desenhado.

# Plotagem do gráfico
ax.plot(x, y) # Desenha o gráfico de "y" (seno de "x") em função de "x" no conjunto de eixos.


#8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?
import pandas as pd #importando pandas como 'pd'
df = pd.read_csv('nome_do_arquivo.csv') # Ler o arquivo CSV em um DataFrame
print(df.head()) # Exibir as primeiras 5 linhas

#9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
import pandas as pd #importando pandas como 'pd'

# Selecionar uma coluna e filtrar linhas com base na condição
coluna_especifica = df['nome_da_coluna']  # Selecionar uma coluna
filtro = df[df['nome_da_coluna'] > valor]  # Filtrar linhas onde 'nome_da_coluna' é maior que um valor
print(filtro)


#10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
import pandas as pd #importando bibiloteca pandas como 'pd'

df.fillna(valor_especifico, inplace=True) # Substituir valores ausentes por um valor específico
df.dropna(inplace=True) # Remover linhas com valores ausentes
print(df.isnull().sum()) # Verificar a presença de valores ausentes


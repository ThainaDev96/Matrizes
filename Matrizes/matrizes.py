
import random

N = 10 # quantidade de linhas
M = 10 # quantidade de colunas

def MostraMatriz(matriz):
    print("  ", end="")
    [print(f" {i:4d}", end="") for i in range(M)]
    print("\n", end="")
    for i in range(N):
        print(i, end=" ")
        for j in range(M):
            print(f" {matriz[i][j]:4d}", end="" )
        print("\n", end="")

def PopulaMatriz(qtLinhas, qtColunas, menorValor, maiorValor):
    matriz = [[0] * qtColunas for i in range(qtLinhas)] # cria a matriz populada com zeros
    for i in range(qtLinhas): # preenche a matriz com inteiros aleatorios
        for j in range(qtColunas):
            matriz[i][j] = random.randint(menorValor, maiorValor)
    return matriz


matriz = PopulaMatriz(N, M, 1, N*M)

MostraMatriz(matriz)




import random  # Importa o módulo random para gerar números aleatórios

N = 10  # Definindo a quantidade de linhas da matriz
M = 10  # Definindo a quantidade de colunas da matriz

# Função para exibir a matriz
def MostraMatriz(matriz):
    print("  ", end="")  # Imprime dois espaços iniciais (para alinhar a exibição dos índices das colunas)
    
    # Exibe os índices das colunas de 0 a M-1 (neste caso, de 0 a 9)
    for i in range(M):  # Loop para imprimir os índices das colunas
        print(f" {i:4d}", end="")  # Formata o índice de cada coluna com 4 espaços de largura
    print()  # Pula uma linha após imprimir os índices das colunas
    
    # Exibe cada linha da matriz
    for i in range(N):  # Loop para percorrer cada linha da matriz
        print(f"{i:2d} ", end="")  # Imprime o índice da linha (formato de 2 dígitos)
        
        for j in range(M):  # Loop para percorrer cada coluna da linha atual
            print(f" {matriz[i][j]:4d}", end="")  # Imprime o valor da célula da matriz com 4 espaços de largura
        print()  # Pula uma linha após imprimir todos os valores de uma linha da matriz

# Função para criar e preencher a matriz com números aleatórios
def PopulaMatriz(qtLinhas, qtColunas, menorValor, maiorValor):
    # Cria uma matriz de zeros, com qtLinhas linhas e qtColunas colunas
    matriz = [[0] * qtColunas for i in range(qtLinhas)]  # Inicializa a matriz com zeros
    
    # Preenche a matriz com números aleatórios entre menorValor e maiorValor
    for i in range(qtLinhas):  # Loop para percorrer as linhas da matriz
        for j in range(qtColunas):  # Loop para percorrer as colunas da linha atual
            matriz[i][j] = random.randint(menorValor, maiorValor)  # Preenche a célula com um número aleatório
    return matriz  # Retorna a matriz preenchida com valores aleatórios

# Cria a matriz de 10x10 com números aleatórios de 1 a N*M (100)
matriz = PopulaMatriz(N, M, 1, N*M)

# Chama a função para exibir a matriz
MostraMatriz(matriz)

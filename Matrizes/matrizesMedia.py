import random
N = 3 # quantidade de linhas
M = 3 # quantidade de colunas

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
            if i==j :
                matriz[i][j] = 0  # Zera a diagonal principal
            else:
                matriz[i][j] = random.randint(menorValor, maiorValor)
    return matriz

def CalculaMedia(matriz):
    soma = 0
    for i in range(N):
        for j in range(M):
            soma+=matriz[i][j]
    return  soma / (N*M) #ou (qtdColunas * qtLinhas)

matriz = PopulaMatriz(N, M, 1, N*M)

MostraMatriz(matriz)
print(CalculaMedia(matriz))
import numpy as np

N = 5  # Tamanho: 5 colunas, 4 linhas, 3 fatias

# Função para mostrar a matriz 3D
def MostraMatriz(matriz, titulo):
    print(f"\n{titulo}")
    for y in range(matriz.shape[1]):  # linhas
        for z in range(matriz.shape[0]):  # fatias
            for x in range(matriz.shape[2]):  # colunas
                print(f"{matriz[z, y, x]:3d}", end=' ')
            print("   ", end="")
        print()

# Popula a matriz com valores sequenciais ou aleatórios
def PopulaMatriz(qtColunas, qtLinhas, qtFatias, menorValor, maiorValor, contagem):
    if contagem:
        matriz = np.arange(1, qtFatias * qtLinhas * qtColunas + 1)
        matriz = matriz.reshape((qtFatias, qtLinhas, qtColunas))
    else:
        matriz = np.random.randint(menorValor, maiorValor + 1,
                                   size=(qtFatias, qtLinhas, qtColunas))
    return matriz

# Exercício 1: Soma dos elementos
def SomaElementos(matriz):
    return np.sum(matriz)

# Exercício 2: Máximo e Mínimo
def EncontraMaxMin(matriz):
    return np.max(matriz), np.min(matriz)

# Exercício 3: Transpor fatias (linha vira coluna e vice-versa)
def TransporFatias(matriz):
    return np.transpose(matriz, axes=(0, 2, 1))  # fatia, coluna, linha

# Exercício 4: Média dos elementos de uma camada específica
def MediaCamada(matriz, indice):
    return np.mean(matriz[indice])

# Exercício 5: Adicionar um valor a todos os elementos
def AdicionarValor(matriz, valor):
    return matriz + valor

# ============================
# Execução principal
# ============================

Ma = PopulaMatriz(N, N-1, N-2, 1, 30, True)
MostraMatriz(Ma, "Matriz 3D Original")

# Exercício 1
print("\nExercício 1 - Soma dos elementos:", SomaElementos(Ma))

# Exercício 2
maximo, minimo = EncontraMaxMin(Ma)
print("Exercício 2 - Máximo:", maximo)
print("Exercício 2 - Mínimo:", minimo)

# Exercício 3
transposta = TransporFatias(Ma)
MostraMatriz(transposta, "Exercício 3 - Fatias Transpostas")

# Exercício 4
media = MediaCamada(Ma, 0)
print("Exercício 4 - Média da camada 0:", media)

# Exercício 5
matriz_adicionada = AdicionarValor(Ma, 10)
MostraMatriz(matriz_adicionada, "Exercício 5 - Matriz com +10 em todos os elementos")

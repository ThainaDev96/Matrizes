import random
N = 5  # Tamanho da matriz: 5 colunas, 4 linhas, 3 fatias (5, 5-1, 5-2)

# Função para mostrar a matriz 3D
def MostraMatriz(matriz, titulo):
    print("\n" + titulo)
    for y in range(len(matriz[0])):  # linhas
        for z in range(len(matriz)):  # fatias
            for x in range(len(matriz[0][y])):  # colunas
                print(f" {matriz[z][y][x]:3d} ", end='')
            print("   ", end="")
        print()

# Função para popular a matriz 3D com valores sequenciais ou aleatórios
def PopulaMatriz(qtColunas, qtLinhas, qtFatias, menorValor, maiorValor, contagem):
    cont = 0
    matriz = []
    for z in range(qtFatias):
        grade = []
        for y in range(qtLinhas):
            linha = []
            for x in range(qtColunas):
                if contagem:
                    cont += 1
                    linha.append(cont)
                else:
                    linha.append(random.randint(menorValor, maiorValor))
            grade.append(linha)
        matriz.append(grade)
    return matriz

# Exercício 1: Soma de todos os elementos
def SomaElementos(matriz):
    soma = 0
    for fatia in matriz:
        for linha in fatia:
            for valor in linha:
                soma += valor
    return soma

# Exercício 2: Encontrar valor máximo e mínimo
def EncontraMaxMin(matriz):
    maximo = matriz[0][0][0]
    minimo = matriz[0][0][0]
    for fatia in matriz:
        for linha in fatia:
            for valor in linha:
                if valor > maximo:
                    maximo = valor
                if valor < minimo:
                    minimo = valor
    return maximo, minimo

# Exercício 3: Transpor cada fatia (linha vira coluna e vice-versa)
def TransporFatias(matriz):
    nova_matriz = []
    for fatia in matriz:
        transposta = []
        for i in range(len(fatia[0])):  # número de colunas vira número de linhas
            nova_linha = []
            for j in range(len(fatia)):  # número de linhas vira número de colunas
                nova_linha.append(fatia[j][i])
            transposta.append(nova_linha)
        nova_matriz.append(transposta)
    return nova_matriz

# Exercício 4: Média dos elementos de uma camada específica
def MediaCamada(matriz, indice):
    camada = matriz[indice]
    soma = 0
    total = 0
    for linha in camada:
        for valor in linha:
            soma += valor
            total += 1
    media = soma / total
    return media

# Exercício 5: Adicionar um valor a todos os elementos
def AdicionarValor(matriz, valor):
    nova_matriz = []
    for fatia in matriz:
        nova_fatia = []
        for linha in fatia:
            nova_linha = []
            for elemento in linha:
                nova_linha.append(elemento + valor)
            nova_fatia.append(nova_linha)
        nova_matriz.append(nova_fatia)
    return nova_matriz

# ============================
# Código principal (execução)
# ============================

# Cria a matriz 3D com valores sequenciais
Ma = PopulaMatriz(N, N-1, N-2, 1, 30, True)

# Exibe a matriz original
MostraMatriz(Ma, "Matriz 3D Original")

# Exercício 1: Soma
print("\nExercício 1 - Soma dos elementos:", SomaElementos(Ma))

# Exercício 2: Máximo e Mínimo
maximo, minimo = EncontraMaxMin(Ma)
print("Exercício 2 - Máximo:", maximo)
print("Exercício 2 - Mínimo:", minimo)

# Exercício 3: Transpor fatias
transposta = TransporFatias(Ma)
MostraMatriz(transposta, "Exercício 3 - Fatias Transpostas")

# Exercício 4: Média dos elementos da camada 0
media = MediaCamada(Ma, 0)
print("Exercício 4 - Média da camada 0:", media)

# Exercício 5: Adicionar +10 a todos os elementos
matriz_adicionada = AdicionarValor(Ma, 10)
MostraMatriz(matriz_adicionada, "Exercício 5 - Matriz com +10 em todos os elementos")

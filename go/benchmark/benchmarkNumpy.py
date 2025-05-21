import numpy as np

def criar_matriz(linhas, colunas):
    # Cria uma matriz com valores sequenciais de 0 até (linhas*colunas - 1)
    return np.arange(linhas * colunas).reshape((linhas, colunas))

def multiplicar_matriz(matriz, fator):
    # Multiplica todos os elementos da matriz por um fator
    return matriz * fator

# Uso
original = criar_matriz(21000, 21000)
multiplicada = multiplicar_matriz(original, 42)

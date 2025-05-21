def criar_matriz(linhas, colunas):
    contador = 0
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(contador)
            contador += 1
        matriz.append(linha)
    return matriz

def multiplicar_matriz(matriz, fator):
    nova_matriz = []
    for linha in matriz:
        nova_linha = []
        for elemento in linha:
            novo_valor = elemento * fator
            nova_linha.append(novo_valor)
        nova_matriz.append(nova_linha)
    return nova_matriz

# Uso
original = criar_matriz(2, 2)
multiplicada = multiplicar_matriz(original, 42)


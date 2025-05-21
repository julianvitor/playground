package main

func criarMatriz(linhas, colunas int) [][]int {
	matriz := make([][]int, linhas)
	contador := 0

	for i := 0; i < linhas; i++ {
		matriz[i] = make([]int, colunas)
		for j := 0; j < colunas; j++ {
			matriz[i][j] = contador
			contador++
		}
	}
	return matriz
}

func multiplicarMatriz(matriz [][]int, fator int) [][]int {
	linhas := len(matriz)
	colunas := len(matriz[0])
	novaMatriz := make([][]int, linhas)

	for i := 0; i < linhas; i++ {
		novaMatriz[i] = make([]int, colunas)
		for j := 0; j < colunas; j++ {
			novaMatriz[i][j] = matriz[i][j] * fator
		}
	}
	return novaMatriz
}

func main() {
	original := criarMatriz(21000, 21000) //
	multiplicada := multiplicarMatriz(original, 42)
	_ = multiplicada[0][0]
}

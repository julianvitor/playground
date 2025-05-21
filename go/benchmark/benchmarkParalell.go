package main

import (
	"fmt"
	"sync"
)

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

func multiplicarMatrizParalela(matriz [][]int, fator int, numGoroutines int) [][]int {
	linhas := len(matriz)
	colunas := len(matriz[0])
	novaMatriz := make([][]int, linhas)

	// Inicializa as linhas da nova matriz para evitar data race
	for i := 0; i < linhas; i++ {
		novaMatriz[i] = make([]int, colunas)
	}

	var wg sync.WaitGroup
	wg.Add(numGoroutines)

	// Determina quantas linhas cada goroutine vai processar
	tamanhoBloco := linhas / numGoroutines

	for g := 0; g < numGoroutines; g++ {
		// Calcula início e fim das linhas para essa goroutine
		inicio := g * tamanhoBloco
		fim := inicio + tamanhoBloco

		// A última goroutine pode pegar as linhas restantes
		if g == numGoroutines-1 {
			fim = linhas
		}

		go func(inicio, fim int) {
			defer wg.Done()
			for i := inicio; i < fim; i++ {
				for j := 0; j < colunas; j++ {
					novaMatriz[i][j] = matriz[i][j] * fator
				}
			}
		}(inicio, fim)
	}

	wg.Wait()
	return novaMatriz
}

func main() {
	original := criarMatriz(21000, 21000)
	multiplicada := multiplicarMatrizParalela(original, 42, 6)
	fmt.Println("Exemplo: elemento [0][0] =", multiplicada[0][0])
}

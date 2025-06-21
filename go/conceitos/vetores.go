package main

import "fmt"

func main() {
	//array
	var vetor [3]int
	vetor[0] = 1
	vetor[1] = 2
	vetor[2] = 3
	fmt.Println(vetor)

	//array com inicialização, declara e aloca valores
	vetor2 := [3]int{1, 2, 3}
	fmt.Println(vetor2)

	// Acessando o valor de um array
	fmt.Println(vetor[0])
	vetor[0] = 10
	fmt.Println(vetor[0])

	// Acessando o tamanho de um array
	fmt.Println(len(vetor))

	//slice, um array dinamico
	var slice []int
	slice = []int{1, 2, 3}
	fmt.Println(slice)

	//slice com inicialização
	slice2 := []int{1, 2, 3}
	fmt.Println(slice2)

	//slice append
	slice2 = append(slice2, 4)
	fmt.Println(slice2)

	//matriz
	matrizSlice := [][]int{
		{1, 2},
		{3, 42},
		{7, 8},
	}
	fmt.Print(matrizSlice[1][1])

}

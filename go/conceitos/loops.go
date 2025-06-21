package main

import "fmt"

func main() {

	a := 1
	for a < 5 { // Semelhante a while
		fmt.Println(a)
		a++
	}

	for indice := 0; indice < 5; indice++ {
		fmt.Println(indice)
	}
}

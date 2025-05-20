package main

import (
	"fmt"
	"math"
	"os"
	"runtime"
	"strconv"
	"sync"
)

func trabalhoPesado(id int, wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Printf("Goroutine #%d iniciada\n", id)

	x := float64(id + 1)
	for {
		// Cálculo pesado em CPU: simula carga usando operações matemáticas
		x = math.Sin(x) * math.Cos(x) * math.Tan(x)
		if math.IsNaN(x) || math.IsInf(x, 0) {
			x = float64(id + 1) // reinicia se der overflow
		}
	}
}

func main() {
	// Define número de goroutines: padrão 4
	numGoroutines := 4
	if len(os.Args) > 1 {
		if n, err := strconv.Atoi(os.Args[1]); err == nil && n > 0 {
			numGoroutines = n
		}
	}

	// Usa todos os núcleos disponíveis
	runtime.GOMAXPROCS(runtime.NumCPU())

	var wg sync.WaitGroup
	wg.Add(numGoroutines)

	for i := 0; i < numGoroutines; i++ {
		go trabalhoPesado(i, &wg)
	}

	wg.Wait() // nunca termina, já que o loop é infinito
}

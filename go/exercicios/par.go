package main

import "fmt"

func main() {
	var a int
	fmt.Scan(&a)
	b := a % 2
	if b > 0 {
		fmt.Println("impar")
	} else {
		fmt.Println("par")
	}
}

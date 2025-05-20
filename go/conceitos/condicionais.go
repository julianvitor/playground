package main

import "fmt"

func main(){
	a := 1
	b := 2
	var c int
	if b>a {
		fmt.Println("B é maior que a")
	} else{
		fmt.Println("a é maior que b")
	}
	fmt.Println("insira A")
	fmt.Scan(&a)
	fmt.Println("insira C")
	fmt.Scan(&c)

	if c>a{
		fmt.Println("c é maior que a")
	}else if c<a{
		fmt.Println("c é menor que a")
	}else{
		fmt.Println("c == a")
	}
}
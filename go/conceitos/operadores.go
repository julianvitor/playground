package main

import "fmt"

func main(){
	 var booleano bool = true
	 var booleano2 bool = false
	 fmt.Println(booleano&&booleano2)// v and f = f
	 fmt.Println(booleano||booleano2)// v ou f = v
	 fmt.Println(!booleano)// nãoV = f
}
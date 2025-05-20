package main

import "fmt"

func main() {
	// Tipos básicos
	var booleano bool = true                          // Booleano
	var cadeia string = "isso é uma string"           // String
	var inteiro int = 42                              // Inteiro genérico (32 ou 64 bits, depende do sistema)
	var inteiro8b int8 = 127                          // Inteiro de 8 bits
	var inteiro16b int16 = 32767                      // Inteiro de 16 bits
	var inteiro32b int32 = 2147483647                 // Inteiro de 32 bits
	var inteiro64b int64 = 9223372036854775807        // Inteiro de 64 bits

	// Tipos sem sinal (unsigned)
	var semSinal uint = 42                            // Inteiro sem sinal (tamanho depende do sistema)
	var byteVar byte = 255                            // Byte (alias de uint8)
	var uint8b uint8 = 255                            // Unsigned 8 bits
	var uint16b uint16 = 65535                        // Unsigned 16 bits
	var uint32b uint32 = 4294967295                   // Unsigned 32 bits
	var uint64b uint64 = 18446744073709551615         // Unsigned 64 bits

	// Rune (representa um caractere Unicode, alias de int32)
	var caractere rune = 'æ'

	// Ponto flutuante
	var flutuante32 float32 = 3.14                    // Float de 32 bits
	var flutuante64 float64 = 2.718281828459045       // Float de 64 bits

	// Números complexos
	var complexo64 complex64 = 1 + 2i                 // Complexo com float32
	var complexo128 complex128 = 3.5 + 4.5i           // Complexo com float64

	// Exibe tudo
	fmt.Printf(
		"booleano: %v\ncadeia: %v\ninteiro: %v\nint8: %v\nint16: %v\nint32: %v\nint64: %v\n"+
		"uint: %v\nbyte: %v\nuint8: %v\nuint16: %v\nuint32: %v\nuint64: %v\n"+
		"rune: %v\nfloat32: %v\nfloat64: %v\ncomplex64: %v\ncomplex128: %v\n",
		booleano, cadeia, inteiro, inteiro8b, inteiro16b, inteiro32b, inteiro64b,
		semSinal, byteVar, uint8b, uint16b, uint32b, uint64b,
		caractere, flutuante32, flutuante64, complexo64, complexo128,
	)
}

package main

import "fmt"

func main(){
	program()
}

func program(){
	var TemperatureCelsius float64
	var TemperatureFahrenheit float64
	var Option int
	thermometer := "\U0001F321"


	for{
		fmt.Printf("CONVERTER %s \n", thermometer)
		fmt.Printf("Celcius to Fahrenheit. TYPE 1\nFahrenheit to Celcius. TYPE 2\n ")

		fmt.Scan(&Option)

		if Option == 1{
			fmt.Printf("Insert temperature in Celcius: ")
			fmt.Scan(&TemperatureCelsius)
			TemperatureFahrenheit = celsiusToFahrenheit(TemperatureCelsius)
			fmt.Printf("Temp = %.2f Fahrenheit\n", TemperatureFahrenheit)
		}else if Option==2{
			fmt.Printf("Insert temperature in Fahrenheit: ")
			fmt.Scan(&TemperatureFahrenheit)
			TemperatureCelsius = FahrenheitToCelsius(TemperatureFahrenheit)
			fmt.Printf("Temp = %.2f Celsius\n", TemperatureCelsius)
		}else{
			fmt.Printf("Invalid option.\n")
		}
	}

}

func celsiusToFahrenheit(tCelsius float64) float64{
	return ((tCelsius*9/5)+32)
}
func FahrenheitToCelsius(tFahrenheit float64) float64{
	return ((tFahrenheit-32)*5/9)
}
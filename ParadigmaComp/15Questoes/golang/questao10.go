package main
//Métodos com Nomes Diferentes 
import "fmt"

// Função para somar dois números
func SomarDois(a, b int) int {
	return a + b
}

// Função para somar três números
func SomarTres(a, b, c int) int {
	return a + b + c
}

func main() {
	fmt.Println(SomarDois(1, 2))       // Soma de dois números
	fmt.Println(SomarTres(1, 2, 3))    // Soma de três números
}

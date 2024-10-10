package main
//Métodos Estáticos
import "fmt"

// Função para calcular o fatorial de um número
func Fatorial(n int) int {
	if n == 0 || n == 1 {
		return 1
	}
	return n * Fatorial(n-1)
}

func main() {
	fmt.Println(Fatorial(5))  // Fatorial de 5
}

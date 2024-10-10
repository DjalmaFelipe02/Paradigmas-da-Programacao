package main
//Métodos de Conveniência (Go)
import "fmt"

// Estrutura Produto
type Produto struct {
	Nome  string
	Preco float64
}

// Método que soma os preços de dois produtos
func SomarProdutos(p1, p2 Produto) float64 {
	return p1.Preco + p2.Preco
}

func main() {
	produto1 := Produto{Nome: "Teclado", Preco: 100}
	produto2 := Produto{Nome: "Mouse", Preco: 50}

	fmt.Println(SomarProdutos(produto1, produto2))  // Soma dos preços dos produtos
}

package main

// Herança

import "fmt"

// Interface Animal
type Animal interface {
	Som() string
}

// Estrutura Cachorro
type Cachorro struct{}

func (c Cachorro) Som() string {
	return "O cachorro faz: Au Au"
}

// Estrutura Gato
type Gato struct{}

func (g Gato) Som() string {
	return "O gato faz: Miau"
}

func main() {
	// Exemplo de uso
	var animal Animal

	animal = Cachorro{}
	fmt.Println(animal.Som())

	animal = Gato{}
	fmt.Println(animal.Som())
}

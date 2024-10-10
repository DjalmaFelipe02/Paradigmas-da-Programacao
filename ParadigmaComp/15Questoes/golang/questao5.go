package main

// Polimorfismo

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

func emitirSons(animais []Animal) {
	for _, animal := range animais {
		fmt.Println(animal.Som())
	}
}

func main() {
	// Exemplo de uso
	animais := []Animal{Cachorro{}, Gato{}}
	emitirSons(animais)
}

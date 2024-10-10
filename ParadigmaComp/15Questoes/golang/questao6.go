package main

// Composição

import "fmt"

// Estrutura Motor
type Motor struct {
	Potencia int
}

// Estrutura Carro
type Carro struct {
	Marca  string
	Modelo string
	Motor  Motor
}

func (c Carro) Detalhes() string {
	return fmt.Sprintf("Carro: %s %s, Potência do motor: %d CV", c.Marca, c.Modelo, c.Motor.Potencia)
}

func main() {
	// Exemplo de uso
	motor := Motor{Potencia: 150}
	carro := Carro{Marca: "Toyota", Modelo: "Corolla", Motor: motor}
	fmt.Println(carro.Detalhes())
}

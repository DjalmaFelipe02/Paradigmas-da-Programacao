package main

import "fmt"
// Métodos para Acelerar e Frear

type Carro struct {
	Marca     string
	Modelo    string
	Ano       int
	Velocidade int
}

func (c *Carro) Acelerar(valor int) {
	c.Velocidade += valor
}

func (c *Carro) Frear(valor int) {
	c.Velocidade -= valor
	if c.Velocidade < 0 {
		c.Velocidade = 0
	}
}

func (c Carro) ExibirVelocidade() string {
	return fmt.Sprintf("Velocidade atual: %d km/h", c.Velocidade)
}

func main() {
	carro := Carro{"Toyota", "Corolla", 2020, 0}
	carro.Acelerar(50)
	fmt.Println(carro.ExibirVelocidade())
	carro.Frear(20)
	fmt.Println(carro.ExibirVelocidade())
}

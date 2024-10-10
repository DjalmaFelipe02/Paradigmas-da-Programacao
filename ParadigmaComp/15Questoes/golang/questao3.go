package main

import "fmt"

// Encapsulamento com Classe ContaBancaria

type ContaBancaria struct {
	titular string
	saldo   float64
}

func (c *ContaBancaria) Depositar(valor float64) {
	c.saldo += valor
}

func (c *ContaBancaria) Sacar(valor float64) {
	if valor <= c.saldo {
		c.saldo -= valor
	} else {
		fmt.Println("Saldo insuficiente.")
	}
}

func (c ContaBancaria) ExibirSaldo() string {
	return fmt.Sprintf("Saldo: %.2f", c.saldo)
}

func main() {
	conta := ContaBancaria{titular: "João", saldo: 0}
	conta.Depositar(1000)
	fmt.Println(conta.ExibirSaldo())
	conta.Sacar(500)
	fmt.Println(conta.ExibirSaldo())
	conta.Sacar(600)
}

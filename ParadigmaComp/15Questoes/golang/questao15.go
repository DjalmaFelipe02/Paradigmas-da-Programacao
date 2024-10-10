package main
//Exceções/Erros Personalizados
import (
	"errors"
	"fmt"
)

// Estrutura ContaBancaria
type ContaBancaria struct {
	Saldo float64
}

// Função para sacar dinheiro, retornando erro personalizado
func (c *ContaBancaria) Sacar(valor float64) error {
	if valor > c.Saldo {
		return errors.New("saldo insuficiente")
	}
	c.Saldo -= valor
	return nil
}

func main() {
	conta := ContaBancaria{Saldo: 100}

	err := conta.Sacar(150)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("Saque realizado com sucesso")
	}
}

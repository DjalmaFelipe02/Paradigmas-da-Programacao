package main

// Agregação

import "fmt"

// Estrutura Empregado
type Empregado struct {
	Nome   string
	Cargo  string
	Salario float64
}

// Estrutura Empresa
type Empresa struct {
	Nome      string
	Empregados []Empregado
}

func (e *Empresa) AdicionarEmpregado(empregado Empregado) {
	e.Empregados = append(e.Empregados, empregado)
}

func (e Empresa) ExibirEmpregados() {
	for _, empregado := range e.Empregados {
		fmt.Printf("Nome: %s, Cargo: %s, Salário: %.2f\n", empregado.Nome, empregado.Cargo, empregado.Salario)
	}
}

func main() {
	empresa := Empresa{Nome: "Tech Corp"}
	empregado1 := Empregado{"Alice", "Desenvolvedora", 5000}
	empregado2 := Empregado{"Bob", "Gerente", 7000}

	empresa.AdicionarEmpregado(empregado1)
	empresa.AdicionarEmpregado(empregado2)

	empresa.ExibirEmpregados()
}

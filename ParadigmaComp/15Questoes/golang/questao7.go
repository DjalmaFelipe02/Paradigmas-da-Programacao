package main

// Associação

import "fmt"

// Estrutura Professor
type Professor struct {
	Nome    string
	Escolas []*Escola
}

func (p *Professor) AdicionarEscola(escola *Escola) {
	p.Escolas = append(p.Escolas, escola)
}

// Estrutura Escola
type Escola struct {
	Nome       string
	Professores []*Professor
}

func (e *Escola) AdicionarProfessor(professor *Professor) {
	e.Professores = append(e.Professores, professor)
	professor.AdicionarEscola(e)
}

func main() {
	// Exemplo de uso
	professor1 := &Professor{Nome: "Dr. João"}
	professor2 := &Professor{Nome: "Prof. Maria"}

	escola1 := &Escola{Nome: "Escola A"}
	escola2 := &Escola{Nome: "Escola B"}

	escola1.AdicionarProfessor(professor1)
	escola1.AdicionarProfessor(professor2)
	escola2.AdicionarProfessor(professor1)

	// Professores da Escola A
	for _, professor := range escola1.Professores {
		fmt.Println(professor.Nome)
	}

	// Professores da Escola B
	for _, professor := range escola2.Professores {
		fmt.Println(professor.Nome)
	}

	// Escolas onde o Dr. João leciona
	for _, escola := range professor1.Escolas {
		fmt.Println(escola.Nome)
	}
}

package main

// Interfaces/Protocolos

import "fmt"

// Interface Imprimivel
type Imprimivel interface {
	Imprimir() string
}

// Estrutura Relatorio
type Relatorio struct{}

func (r Relatorio) Imprimir() string {
	return "Imprimindo Relatório..."
}

// Estrutura Contrato
type Contrato struct{}

func (c Contrato) Imprimir() string {
	return "Imprimindo Contrato..."
}

func executarImpressao(imprimivel Imprimivel) {
	fmt.Println(imprimivel.Imprimir())
}

func main() {
	relatorio := Relatorio{}
	contrato := Contrato{}

	executarImpressao(relatorio)
	executarImpressao(contrato)
}

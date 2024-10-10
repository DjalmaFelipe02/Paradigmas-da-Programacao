package main

import "fmt"

// Motor struct
type Motor struct {
	tipo    string
	potencia int
}

// Ligar método
func (m *Motor) Ligar() {
	fmt.Println("O motor está ligado")
}

// Desligar método
func (m *Motor) Desligar() {
	fmt.Println("O motor está desligado")
}

// Pneu struct
type Pneu struct {
	marca   string
	tamanho int
}

// Inflar método
func (p *Pneu) Inflar() {
	fmt.Println("O pneu está inflado")
}

// Desinflar método
func (p *Pneu) Desinflar() {
	fmt.Println("O pneu está desinflado")
}

// Carro struct
type Carro struct {
	marca  string
	modelo string
	motor  Motor
	pneus  []Pneu
}

// Ligar método
func (c *Carro) Ligar() {
	c.motor.Ligar()
	fmt.Println("O carro está pronto para rodar")
}

// Desligar método
func (c *Carro) Desligar() {
	c.motor.Desligar()
	fmt.Println("O carro foi desligado")
}

// TrocarPneu método
func (c *Carro) TrocarPneu(indice int, novoPneu Pneu) {
	c.pneus[indice] = novoPneu
	fmt.Printf("Pneu %d trocado\n", indice+1)
}

// Função principal
func main() {
	carro := Carro{
		marca:  "Toyota",
		modelo: "Corolla",
		motor:  Motor{tipo: "Gasolina", potencia: 150},
		pneus:  []Pneu{
			{"Pirelli", 18},
			{"Pirelli", 18},
			{"Pirelli", 18},
			{"Pirelli", 18},
		},
	}

	carro.Ligar()

	novoPneu := Pneu{marca: "Michelin", tamanho: 17}
	carro.TrocarPneu(2, novoPneu)

	carro.Desligar()
}

package main
//Classes Abstratas
import "fmt"

// Interface Funcionario
type Funcionario interface {
	CalcularSalario() float64
}

// Estrutura FuncionarioHorista
type FuncionarioHorista struct {
	Horas      int
	ValorHora  float64
}

func (f FuncionarioHorista) CalcularSalario() float64 {
	return float64(f.Horas) * f.ValorHora
}

// Estrutura FuncionarioAssalariado
type FuncionarioAssalariado struct {
	SalarioFixo float64
}

func (f FuncionarioAssalariado) CalcularSalario() float64 {
	return f.SalarioFixo
}

func main() {
	horista := FuncionarioHorista{Horas: 160, ValorHora: 20}
	assalariado := FuncionarioAssalariado{SalarioFixo: 3000}

	fmt.Println(horista.CalcularSalario())  // Salário do horista
	fmt.Println(assalariado.CalcularSalario())  // Salário do assalariado
}

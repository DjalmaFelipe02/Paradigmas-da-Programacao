package main
//Singleton
import "fmt"

// Estrutura Singleton
type Configuracao struct{}

var instancia *Configuracao

func GetConfiguracao() *Configuracao {
	if instancia == nil {
		instancia = &Configuracao{}
	}
	return instancia
}

func main() {
	config1 := GetConfiguracao()
	config2 := GetConfiguracao()

	fmt.Println(config1 == config2)  // True (mesma instância)
}

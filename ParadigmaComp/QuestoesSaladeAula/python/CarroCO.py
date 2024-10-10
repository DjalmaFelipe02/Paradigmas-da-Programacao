class Motor:
    def __init__(self, tipo, potencia) -> None:
        self.tipo = tipo
        self.potencia = potencia
    
    def ligar(self):
        print("O motor esta ligado")

    def desligar(self):
        print("O motor esta desligado")

class Pneu:
    def __init__(self, marca, tamanho) -> None:
        self.marca = marca
        self.tamanho = tamanho

    def inflar(self):
        print("O pneu esta inflado")

    def desinflar(self):
        print("O pneu esta desinflado")

class Carro:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("Gasolina", 150) # Composição
        self.pneus = [Pneu("Pirelli", 18) for _ in range(4)] # Composição

    def ligar(self):
        self.motor.ligar()
        print("O carro esta pronto para rodar")

    def desligar(self):
        self.motor.desligar()
        print("O carro foi desligado")

    def trocar_pneu(self, indice, novo_pneu):
        self.pneus[indice] = novo_pneu
        print(f"Pneu {indice + 1} trocado")

def main():
    carro = Carro("Toyota", "Corolla")
    carro.ligar()

    novo_pneu = Pneu("Michelin", 17)
    carro.trocar_pneu(2, novo_pneu)
    carro.desligar()

if __name__ == "__main__":
    main()
# Métodos para Acelerar e Frear
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0

    def exibir_velocidade(self):
        return f"Velocidade atual: {self.velocidade} km/h"

# Exemplo de uso
carro = Carro("Toyota", "Corolla", 2020)
carro.acelerar(50)
print(carro.exibir_velocidade())
carro.frear(20)
print(carro.exibir_velocidade())

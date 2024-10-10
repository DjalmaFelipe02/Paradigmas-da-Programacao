# Classes e Objetos Básicos
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

# Instanciando 3 objetos
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2018)
carro3 = Carro("Ford", "Mustang", 2021)

# Exibindo os detalhes
print(carro1.detalhes())
print(carro2.detalhes())
print(carro3.detalhes())

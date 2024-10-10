# Herança
class Animal:
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        return "O cachorro faz: Au Au"

class Gato(Animal):
    def som(self):
        return "O gato faz: Miau"

# Exemplo de uso
cachorro = Cachorro()
gato = Gato()
print(cachorro.som())
print(gato.som())

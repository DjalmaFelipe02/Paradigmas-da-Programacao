# Polimorfismo
class Animal:
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        return "O cachorro faz: Au Au"

class Gato(Animal):
    def som(self):
        return "O gato faz: Miau"

def emitir_sons(animais):
    for animal in animais:
        print(animal.som())

# Exemplo de uso
animais = [Cachorro(), Gato()]
emitir_sons(animais)

class Animal:
    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau"
    
def main():
    
    print()

if __name__ == "__main__":
    main()
    
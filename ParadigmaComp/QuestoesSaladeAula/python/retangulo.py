class Retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura
    
    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)
    
def main():
    ret = Retangulo(200, 100)
    print("Area: ",  ret.calcular_area())
    print("Perimetro: ", ret.calcular_perimetro())

if __name__ == "__main__":
    main()
    
# Programa python para gerar automaticamente numeros
# entre 0 e 99 de uma cartela de bingo. Sabendo que cada
# cartela deverá ser 5x5, gere estes dados de modo a nao 
# ter numeros repetidos dentro da cartela
# Davi Brito Machado P6
# RGM: 30116104 

import random

def gerarCartela():
    numeros = set()
    cartela = []
    for i in range(5):
        for j in range(5):
            numero = random.randint(0, 99)
            numeros.add(numero)
        cartela.append(numeros)
        numeros.clear()
    return cartela

def main():
    cartela = gerarCartela()
    print("Cartela de bingo: ")
    for linha in cartela:
        print(linha)

if __name__ == "__main__":
    main()
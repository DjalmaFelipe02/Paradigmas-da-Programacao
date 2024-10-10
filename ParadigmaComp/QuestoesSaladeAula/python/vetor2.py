# Programa em python para leitura de um vetor
# com 10 posições. em seguida devera ser impresso 
# o maior, menor elemento e soma de todos
# Davi Brito Machado P6
# RGM: 30116104 

from func import fazLista, maiorEMenor, somaLista

def main():
    vetor = fazLista(10)
    
    maiorEMenor(vetor)
    somaLista(vetor)
    
if __name__ == "__main__":
    main()
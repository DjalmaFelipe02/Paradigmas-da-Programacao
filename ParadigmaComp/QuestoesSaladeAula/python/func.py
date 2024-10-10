def fazLista(x):
    vetor = [0] * x

    for i in range(x):
        vetor[i] = int(input("Digite o valor da posicao {}: ".format(i)))

    return vetor

def leitura():
    return int(input("Digite a posicao: "))

def soma(x, y):
    return print(x + y)

def maiorEMenor(vetor):
    maior = 0
    menor = 99999

    for i in range(0, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
        if vetor[i] < menor:
            menor = vetor[i]
    return print("Maior elemento %d e menor elemento %d" % maior, menor)

def somaLista(vetor):
    soma = 0

    for i in range(0, len(vetor)):
        soma += vetor[i]
    return print("Soma e %d" % soma)
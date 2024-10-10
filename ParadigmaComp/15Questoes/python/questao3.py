# Encapsulamento com Classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        return f"Saldo: {self.__saldo}"

# Exemplo de uso
conta = ContaBancaria("João")
conta.depositar(1000)
print(conta.exibir_saldo())
conta.sacar(500)
print(conta.exibir_saldo())
conta.sacar(600)

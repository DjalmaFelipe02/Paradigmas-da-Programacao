#Exceções/Erros Personalizados
class SaldoInsuficienteException(Exception):
    def __init__(self, mensagem="Saldo insuficiente para a operação"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteException()
        self.saldo -= valor

# Exemplo de uso
conta = ContaBancaria(100)
try:
    conta.sacar(150)
except SaldoInsuficienteException as e:
    print(e)

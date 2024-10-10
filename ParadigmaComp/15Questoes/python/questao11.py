from abc import ABC, abstractmethod
#Classes Abstratas
class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, horas, valor_hora):
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas * self.valor_hora

class FuncionarioAssalariado(Funcionario):
    def __init__(self, salario_fixo):
        self.salario_fixo = salario_fixo

    def calcular_salario(self):
        return self.salario_fixo

# Exemplo de uso
horista = FuncionarioHorista(160, 20)
assalariado = FuncionarioAssalariado(3000)

print(horista.calcular_salario())  # Salário do horista
print(assalariado.calcular_salario())  # Salário do assalariado

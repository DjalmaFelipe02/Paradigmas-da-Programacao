# Agregação

class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []

    def adicionar_empregado(self, empregado):
        self.empregados.append(empregado)

    def exibir_empregados(self):
        for empregado in self.empregados:
            print(f"Nome: {empregado.nome}, Cargo: {empregado.cargo}, Salário: {empregado.salario}")

# Exemplo de uso
empresa = Empresa("Tech Corp")
empregado1 = Empregado("Alice", "Desenvolvedora", 5000)
empregado2 = Empregado("Bob", "Gerente", 7000)

empresa.adicionar_empregado(empregado1)
empresa.adicionar_empregado(empregado2)

empresa.exibir_empregados()

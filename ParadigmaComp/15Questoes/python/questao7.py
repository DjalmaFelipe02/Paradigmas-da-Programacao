# Associação
class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []

    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)

    def exibir_escolas(self):
        return [escola.nome for escola in self.escolas]

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
            professor.adicionar_escola(self)

    def exibir_professores(self):
        return [professor.nome for professor in self.professores]

# Exemplo de uso
professor1 = Professor("Dr. João")
professor2 = Professor("Prof. Maria")

escola1 = Escola("Escola A")
escola2 = Escola("Escola B")

escola1.adicionar_professor(professor1)
escola1.adicionar_professor(professor2)
escola2.adicionar_professor(professor1)

print(escola1.exibir_professores())  # Professores da Escola A
print(escola2.exibir_professores())  # Professores da Escola B
print(professor1.exibir_escolas())   # Escolas onde o Dr. João leciona

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = None

    def adicionar_endereco(self, endereco):
        self.endereco = endereco

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        if self.endereco:
            print("Endereco: ")
            self.endereco.mostrar_endereco()
        else:
            print("Endereco não disponivel")

class Endereco:
    def __init__(self, rua, cidade, estado, cep) -> None:
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
    
    def mostrar_endereco(self):
        print(f"Rua: {self.rua}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}")

class Empresa:
    def __init__(self, nome, cnpj) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self.funcionarios = []

    def contratar_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def listar_funcionarios(self):
        print(f"Funcionarios da empresa {self.nome}:")
        for funcionario in self.funcionarios:
            print(funcionario.nome)

def main():
    endereco1 = Endereco("Av. Principal", "Patapingas", "Minas Gerais", "12345-234")
    pessoa1 = Pessoa("João", 30)
    pessoa1.adicionar_endereco(endereco1)

    endereco2 = Endereco("Av. Secundaria", "Maraja", "Sao paulo", "54321-234")
    pessoa2 = Pessoa("Maria", 25)
    pessoa2.adicionar_endereco(endereco2)

    empresa = Empresa("Empresa ABC", "18509274")
    empresa.contratar_funcionarios(pessoa1)
    empresa.contratar_funcionarios(pessoa2)

    empresa.listar_funcionarios()

if __name__ == "__main__":
    main()
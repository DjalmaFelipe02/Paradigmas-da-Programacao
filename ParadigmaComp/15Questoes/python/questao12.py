#Sobrecarga de Operadores (Python)
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __add__(self, outro):
        return self.preco + outro.preco

# Exemplo de uso
produto1 = Produto("Teclado", 100)
produto2 = Produto("Mouse", 50)

print(produto1 + produto2)  # Soma dos preços dos produtos

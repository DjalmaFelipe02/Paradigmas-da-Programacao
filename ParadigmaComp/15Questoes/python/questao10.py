#Métodos com Nomes Diferentes
class Calculadora:
    def somar(self, a, b):
        return a + b

    def somar_tres(self, a, b, c):
        return a + b + c

# Exemplo de uso
calc = Calculadora()
print(calc.somar(1, 2))       # Soma de dois números
print(calc.somar_tres(1, 2, 3))  # Soma de três números

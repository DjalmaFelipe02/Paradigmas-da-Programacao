# Métodos Estáticos
class Matematica:
    @staticmethod
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * Matematica.fatorial(n - 1)

# Exemplo de uso
print(Matematica.fatorial(5))  # Fatorial de 5

#Singleton
class Configuracao:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

# Exemplo de uso
config1 = Configuracao()
config2 = Configuracao()

print(config1 == config2)  # True (mesma instância)

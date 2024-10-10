from abc import ABC, abstractmethod

# Interfaces/Protocolos

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Relatorio(Imprimivel):
    def imprimir(self):
        return "Imprimindo Relatório..."

class Contrato(Imprimivel):
    def imprimir(self):
        return "Imprimindo Contrato..."

# Exemplo de uso
def executar_impressao(documento: Imprimivel):
    print(documento.imprimir())

relatorio = Relatorio()
contrato = Contrato()

executar_impressao(relatorio)
executar_impressao(contrato)

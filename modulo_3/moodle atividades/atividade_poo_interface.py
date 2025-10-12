# ==========================
# Exercícios - Interfaces em POO (Python)
# ==========================

from abc import ABC, abstractmethod

# Exercício 1 - Criando uma Interface
# Crie uma interface chamada Pagamento com um método abstrato processar(valor).
# Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface.
# Mostre como chamar processar() para cada uma.
class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"Processando pagamento de {valor} via Cartão de Crédito."


class Boleto(Pagamento):
    def processar(self,valor):
        return f"Processando pagamento de {valor} via Boleto."
    
def realizar_pagamento(metodo:Pagamento,valor):
    return metodo.processar(valor)

print (realizar_pagamento(CartaoCredito(),(100)))
print (realizar_pagamento(Boleto(),(200)))

# ==========================
# Exercício 2 - Interface Múltipla
# Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()).
# Crie uma classe Computador que implemente ambas. Mostre seu uso.
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass    

class Computador(Ligavel, Desligavel):
    def ligar(self):
        return "Computador ligado."

    def desligar(self):
        return "Computador desligado."
    

print(Computador().ligar())
print(Computador().desligar())

# ==========================
# Exercício 3 - Interface em Herança Múltipla
# Crie uma interface Imprimivel com o método imprimir().
# Crie outra interface Exportavel com o método exportar().
# Implemente uma classe Relatorio que herde de ambas e implemente os métodos.
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self, formato):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        return "Imprimindo relatório."

    def exportar(self, formato):
        return f"Exportando relatório em {formato}."

relatorio = Relatorio()
print(relatorio.imprimir())
print(relatorio.exportar("PDF"))

# ==========================
# Exercício 4 - Forçando Contrato
# Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id).
# Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos.
# O que acontece quando você tenta instanciá-la? Corrija o código.
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Objeto {objeto} salvo na memória.")

try :
   repositorio=RepositorioMemoria()
except TypeError as e:
    print("\nErro ao tentar instanciar RepositorioMemoria:")
    print(e)
    print("➡ Ambos os métodos 'salvar' e 'carregar' precisam ser implementados.")

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Objeto {objeto} salvo na memória.")

    def buscar(self, id):
        print(f"Buscando objeto com id {id} na memória.")
        return {"id": id, "nome": "Exemplo"}

repositorio = RepositorioMemoria()
repositorio.salvar({"id": 1, "nome": "Teste"})
obj = repositorio.buscar(1)
print(obj)
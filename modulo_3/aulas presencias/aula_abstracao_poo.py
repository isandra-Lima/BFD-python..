# ==========================
# Abstração em POO
# ==========================
# Abstração é o princípio de mostrar apenas o que é essencial e esconder os detalhes internos.
# Serve para simplificar o código e evitar que o usuário precise conhecer o funcionamento interno.

# ==========================
# Classe Abstrata (ABC)
# ==========================
# ABC = Abstract Base Class → usada para criar classes modelo.
# Uma classe abstrata NÃO pode ser usada diretamente, apenas servindo de base para outras classes.
# É criada herdando de 'ABC' do módulo 'abc'.
#
# Sintaxe:
# from abc import ABC
# class MinhaClasse(ABC):
#     pass
#
# Uso: definir uma estrutura que outras classes devem seguir.

# ==========================
# Método Abstrato (@abstractmethod)
# ==========================
# É um método obrigatório que toda classe filha deve implementar.
# Serve para garantir que todas as classes filhas tenham o mesmo conjunto mínimo de métodos.
#
# Sintaxe:
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def falar(self):
#         pass
#
# class Cachorro(Animal):
#     def falar(self):
#         print("Au au!")
#
# dog = Cachorro()
# dog.falar()  # "Au au!"
#
# Se tentarmos criar um objeto de Animal, o Python dará erro:
# TypeError: Can't instantiate abstract class Animal with abstract method falar
#
# Uso: criar um “modelo” obrigatório para classes filhas.

# ==========================
# RESUMO FINAL
# ==========================
# Abstração → mostra só o essencial e esconde o complexo.
# ABC → cria uma classe modelo (não pode ser instanciada).
# @abstractmethod → cria métodos obrigatórios nas classes filhas.
# Classe abstrata → receita de bolo (não é usada direto).
# Classe filha → bolo pronto (usa e completa a receita).

# ==========================
# Exercícios - Abstração e Classes Abstratas - sala
# ==========================

# Exercício 1: Classe Abstrata "Animal"
# Crie uma classe abstrata chamada "Animal" com um método abstrato "falar()".
# Depois, crie duas classes filhas: "Cachorro" e "Gato".
# Cada uma deve implementar o método "falar()" de forma diferente.
#
# Dica: use from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

# Teste
dog = Cachorro()
cat = Gato()
dog.falar()  # Au au!
cat.falar()  # Miau!



# ==========================
# Exercício 2: Classe Abstrata "Forma"
# ==========================
# Crie uma classe abstrata chamada "Forma" com um método abstrato "area()".
# Depois, crie duas classes filhas:
# - "Quadrado", que recebe o lado e calcula a área (lado * lado)
# - "Circulo", que recebe o raio e calcula a área (3.14 * raio * raio)
#
# Mostre a área de um quadrado e de um círculo.

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio * self.raio

# Teste
q = Quadrado(4)
c = Circulo(3)
print("\nÁrea do quadrado:", q.area())
print("Área do círculo:", c.area())

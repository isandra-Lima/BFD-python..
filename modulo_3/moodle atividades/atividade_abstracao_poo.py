# ==========================
# Exercícios - Abstração e Classes Abstratas (ABC e @abstractmethod)
# ==========================

from abc import ABC,abstractmethod

# Exercício 1 - Classe Abstrata Animal
# Cria uma classe abstrata Animal com o método abstrato falar().
# As classes Cachorro e Gato herdam e implementam o método de forma diferente.
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
dog.falar()  
cat.falar()  

# Exercício 2 - Proibição de Instanciamento
# Mostra que não é possível instanciar uma classe abstrata diretamente.
# O Python gera um erro: "TypeError: Can't instantiate abstract class..."
try:
    bicho = Animal()  # Erro proposital
except TypeError as e:
    print("\nErro ao tentar instanciar Animal:")
    print(e)
    print("➡ Animal é abstrata e não pode ser instanciada.")


# Exercício 3 - Múltiplos Métodos Abstratos
# Define a classe abstrata FormaGeometrica com dois métodos abstratos:
# area() e perimetro(). A classe Retangulo implementa ambos.
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        return  self.base * self.altura
    
retangulo=Retangulo(5,10)
print(retangulo.area())

# Exercício 4 - Herança Parcial
# Cria uma classe abstrata Transporte com dois métodos: mover() e parar().
# A subclasse Carro implementa apenas um deles (mover), causando erro.
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
    @abstractmethod
    def parar(self):
        pass 

class Carro(Transporte):
    def mover (self):
        print("O carro está se movendo")


try:
    c = Carro()
except TypeError as e:
    print("\nErro ao tentar instanciar Carro:")
    print(e)
    print("➡ O método 'parar()' não foi implementado, então a classe ainda é abstrata.")

# Corrigindo:
class Carro(Transporte):
    def mover(self):
        print("O carro está se movendo!")

    def parar(self):
        print("O carro parou.")

c = Carro()
print("\nTeste com Carro corrigido:")
c.mover()
c.parar()
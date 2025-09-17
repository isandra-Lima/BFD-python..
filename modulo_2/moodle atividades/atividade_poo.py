# ==========================
# Exercícios de Classes
# ==========================

# Exercício 1 - Criando a classe Pessoa
# Cria a classe Pessoa com os atributos nome e idade
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto da classe Pessoa
p1 = Pessoa("João", 25)
print(f"Nome da pessoa: {p1.nome}")
print(f"Idade da pessoa: {p1.idade}")

# Exercício 2 - Adicionando método apresentar
# Cria um método para mostrar uma mensagem apresentando a pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

p2 = Pessoa("João", 25)
p2.apresentar()

# Exercício 3 - Criando a classe Carro
# Cria a classe Carro com atributos marca, modelo e ano
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_mensagem(self):
        print(f"Seu carro é {self.marca}, {self.modelo} de {self.ano}")

carro1 = Carro("Toyota", "Corola", 2012)
carro1.exibir_mensagem()

# Exercício 4 - Alterar o atributo de um objeto
# Mostra como alterar o ano de um carro após a criação
print("Antes:", carro1.ano)
carro1.ano = 2020
print("Depois:", carro1.ano)

# Exercício 5 - Criando a classe ContaBancaria
# Cria uma classe com métodos para depositar, sacar e exibir saldo
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo atual: R${self.saldo}")

cliente = ContaBancaria("Maria", 250)
cliente.exibir_saldo()
cliente.sacar(100)

# Exercício 6 - Criando classes Aluno e Turma
# Cria a classe Aluno com nome e nota, e Turma que guarda alunos
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

# Criando objetos Aluno
a1 = Aluno("Maria", 9.5)
a2 = Aluno("João", 8.7)
a3 = Aluno("Ana", 7.8)

# Criando uma turma e adicionando alunos
turma = Turma()
turma.adicionar_aluno(a1)
turma.adicionar_aluno(a2)
turma.adicionar_aluno(a3)

print("\nAlunos na turma:")
for aluno in turma.alunos:
    print(aluno)

# Exercício 7 - Atributos de classe e instância
# Mostra a diferença entre atributo de classe e atributo de instância
class Cachorro:
    especie = "Canis familiaris"  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

dog = Cachorro("Rex", 5)

print("\nAcessando atributo de classe:")
print("Pelo objeto:", dog.especie)
print("Pela classe:", Cachorro.especie)

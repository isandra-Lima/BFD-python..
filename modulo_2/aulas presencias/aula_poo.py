# ==========================================================
#  POO -(Programação Orientada a Objetos)
# ==========================================================

# ----------------------------------------------------------
# 1) CLASSE
# Uma classe é como um "molde" ou "planta baixa" que define
# como os objetos serão. Ela descreve ATRIBUTOS (características)
# e MÉTODOS (ações).
# ----------------------------------------------------------

class Pessoa:
    # ------------------------------------------------------
    # 2) MÉTODO CONSTRUTOR (__init__)
    # Esse método é chamado automaticamente quando criamos
    # um novo objeto. Ele inicializa os atributos.
    # ------------------------------------------------------
    def __init__(self, nome, idade):
        self.nome = nome      # atributo: nome da pessoa
        self.idade = idade    # atributo: idade da pessoa

    # ------------------------------------------------------
    # 3) MÉTODOS
    # São funções definidas dentro da classe que descrevem
    # comportamentos/ações que o objeto pode realizar.
    # ------------------------------------------------------
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# ----------------------------------------------------------
# 4) OBJETOS
# Um objeto é uma "cópia" (instância) criada a partir da classe.
# Cada objeto tem seus próprios atributos e pode executar métodos.
# ----------------------------------------------------------

p1 = Pessoa("Ana", 25)     # Criando objeto 1
p2 = Pessoa("Carlos", 30)  # Criando objeto 2

# ----------------------------------------------------------
# Usando os MÉTODOS do objeto
# ----------------------------------------------------------
print(p1.apresentar())  # Saída: Olá, meu nome é Ana e tenho 25 anos.
print(p2.apresentar())  # Saída: Olá, meu nome é Carlos e tenho 30 anos.


# ==========================================================
#   PRINCIPAIS PILARES DA POO
# ==========================================================

# ----------------------------------------------------------
# 5) ENCAPSULAMENTO
# É a forma de proteger atributos para que não sejam
# acessados diretamente de fora da classe.
# Usa-se "__" (dois underlines) para torná-los privados.
# ----------------------------------------------------------

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo   # atributo privado (encapsulado)

    # Método público para acessar o saldo de forma segura
    def ver_saldo(self):
        return f"Saldo atual: R${self.__saldo}"

    # Método público para alterar o saldo de forma controlada
    def depositar(self, valor):
        self.__saldo += valor
        return f"Depósito realizado. Novo saldo: R${self.__saldo}"

conta = ContaBancaria("João", 1000)
print(conta.ver_saldo())   # Acessando saldo de forma segura
print(conta.depositar(500))
# print(conta.__saldo)    # ERRO: não pode acessar diretamente


# ----------------------------------------------------------
# 6) HERANÇA
# Permite que uma classe "filha" herde atributos e métodos
# de uma classe "pai". Assim, reutilizamos código.
# ----------------------------------------------------------

class Estudante(Pessoa):  # Estudante herda de Pessoa
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # reaproveita o construtor da classe pai
        self.curso = curso

    # Método novo só da classe filha
    def apresentar(self):
        # Polimorfismo: mesmo nome de método, mas comportamento diferente
        return f"Sou {self.nome}, tenho {self.idade} anos e estudo {self.curso}."

e1 = Estudante("Maria", 20, "Engenharia")
print(e1.apresentar())  # Saída: Sou Maria, tenho 20 anos e estudo Engenharia.


# ----------------------------------------------------------
# 7) POLIMORFISMO
# É quando um mesmo método (mesmo nome) pode ter comportamentos
# diferentes dependendo da classe onde está implementado.
# Ex: "apresentar()" funciona diferente em Pessoa e Estudante.
# ----------------------------------------------------------


# ==========================================================
# RESUMO FINAL
# ----------------------------------------------------------
# Classe        -> Molde para criar objetos
# Objeto        -> Instância da classe (cópia real)
# Atributos     -> Características do objeto
# Métodos       -> Ações do objeto
# Encapsulamento-> Proteção de dados
# Herança       -> Reaproveitamento de código
# Polimorfismo  -> Métodos com mesmo nome, mas diferentes ações
# ==========================================================










#=========================
#Exercicio de Poo - Aula
#=========================
# ==========================
# Exercícios - POO - sala
# ==========================

# Exercício 1: Criar uma classe Carro
# Crie uma classe chamada Carro com os atributos modelo e ano.
# Crie um método descricao() que retorna uma string com o modelo e ano.

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano}"

# Testando
carro1 = Carro("Civic", 2020)
print(carro1.descricao())


# Exercício 2: Encapsulamento com Conta Bancaria
# Crie uma classe Conta com atributo saldo privado.
# Crie métodos para ver_saldo(), depositar(valor) e sacar(valor).

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # saldo privado

    def ver_saldo(self):
        return f"Saldo atual: R${self.__saldo}"

    def depositar(self, valor):
        self.__saldo += valor
        return f"Depósito realizado. Novo saldo: R${self.__saldo}"

    def sacar(self, valor):
        if valor > self.__saldo:
            return "Saldo insuficiente"
        self.__saldo -= valor
        return f"Saque realizado. Novo saldo: R${self.__saldo}"

# Testando
conta1 = Conta("João", 1000)
print(conta1.ver_saldo())
print(conta1.depositar(500))
print(conta1.sacar(200))
print(conta1.sacar(2000))  # tenta sacar mais que o saldo


# Exercício 3: Herança e Polimorfismo
# Crie uma classe Funcionario com nome e salario e um método mostrar_dados()
# Crie uma classe Gerente que herda de Funcionario e adiciona departamento
# Sobrescreva mostrar_dados() na classe Gerente

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_dados(self):
        return f"Nome: {self.nome}, Salário: {self.salario}"

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def mostrar_dados(self):
        return f"Nome: {self.nome}, Salário: {self.salario}, Departamento: {self.departamento}"

# Testando
f1 = Funcionario("Ana", 3000)
g1 = Gerente("Carlos", 5000, "Vendas")

print(f1.mostrar_dados())
print(g1.mostrar_dados())


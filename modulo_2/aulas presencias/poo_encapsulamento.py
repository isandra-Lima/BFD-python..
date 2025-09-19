# ==========================
# POO- Encapsulamento 
# ==========================

# RESUMO: Encapsulamento
# Encapsulamento é proteger os dados internos de um objeto,
# tornando atributos privados (__atributo) e acessando-os de forma controlada.
# Para isso usamos:
# - Getter: método para ler o valor do atributo
# - Setter: método para alterar o valor do atributo com validação


# ==========================
# Exercícios - Encapsulamento - sala
# ==========================

# Exercício 1: Classe Pessoa com getter e setter
# Crie uma classe Pessoa com atributo privado __nome e métodos para ler e alterar o nome
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    # Getter
    def get_nome(self):
        return self.__nome

    # Setter
    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            print("Nome inválido!")

# Criando objeto e testando
p = Pessoa("João")
print("Nome inicial:", p.get_nome())
p.set_nome("Maria")
print("Nome atualizado:", p.get_nome())
p.set_nome("")  # Tentativa inválida

# Exercício 2: Classe ContaBancaria com saldo protegido
# Crie uma classe ContaBancaria com saldo privado, getter para ler e setter para alterar com validação
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo inválido!")

# Criando objeto e testando
conta = ContaBancaria(500)
print("\nSaldo inicial:", conta.get_saldo())
conta.set_saldo(1000)
print("Saldo atualizado:", conta.get_saldo())
conta.set_saldo(-50)  # Tentativa inválida

# Exercício 3: Classe Produto com nome e preço privados
# Crie uma classe Produto com atributos privados __nome e __preco, getters e setters com validação
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            print("Nome inválido!")

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco > 0:
            self.__preco = preco
        else:
            print("Preço inválido!")

# Criando objeto e testando
produto = Produto("Caneta", 2.5)
print("\nProduto:", produto.get_nome(), "- Preço:", produto.get_preco())
produto.set_preco(3.0)
print("Preço atualizado:", produto.get_preco())
produto.set_preco(-1)  
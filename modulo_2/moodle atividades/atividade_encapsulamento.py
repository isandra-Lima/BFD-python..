# ==========================
# Exercícios de Encapsulamento
# ==========================

# Exercício 1 - Criando a classe Pessoa com atributos privados
# Cria a classe Pessoa com os atributos nome e data de nascimento públicos
# e cpf e identidade privados
class ContaBancaria:
   def __init__(self,titular,saldo=0):
      self.titular = titular
      self.__saldo=saldo

   def get_saldo(self):
        return self.__saldo
   
   def set_saldo(self,valor):
       if valor <=0:
            print("ERROR: Valor inválido")
       else:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado ")
            return self.__saldo

cliente= ContaBancaria("Maria",250)
print('Seu saldo é :',cliente.get_saldo())
print('Seu saldo após alteração é :',cliente.set_saldo(100))
cliente.set_saldo(-50)


#Exercício 2 - Criando a classe Pessoa com atributos privados
# Cria a classe Pessoa com os atributos nome, data de nascimento,
# cpf e identidade. Os atributos cpf e identidade são privados (_cpf e _identidade)
# e possuem métodos getter e setter para acessar e modificar seus valores
class Pessoa:
    def __init__(self,nome,data_nascimento,cpf,identidade):
        self.nome=nome
        self.data_nascimento=data_nascimento
        self.__cpf=cpf
        self.__identidade=identidade
    def __str__(self):  
        return f' Nome: {self.nome} - Data de Nascimento: {self.data_nascimento}'
    
    def get__documentos(self):
        return f' CPF: {self.__cpf} - Identidade: {self.__identidade}'
    
    def set__documentos(self,cpf,identidade):
        if len(cpf)==11 and len(identidade)==9:
            self.__cpf=cpf
            self.__identidade=identidade
            return f' \nNovos documentos - CPF: {self.__cpf} - Identidade: {self.__identidade}'
        else:
            print("ERROR: Documentos inválidos")

pessoa=Pessoa("João","01/01/1990","12345678901","123456789")
print(pessoa)
print(pessoa.get__documentos())
print('Seus dados após alterações são:',pessoa.set__documentos("98765432100","987654321"))
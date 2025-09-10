#Exercicio 1
# class Pessoa:
#     def __init__(self,nome,idade):
#         self.nome= nome
#         self.idade=idade
        

#     def exibir_dados_pessoais(self):
#         print('====Dados Pessoais====')
#         print(f'Nome: {self.nome}')
#         print(f'idade : {self.idade}')

#     def exibir_mensagem(self):
#         print(f' O {self.nome} gosta de correr marratona')
    
# p1=Pessoa('joão',25)
# p1.exibir_dados_pessoais()
# p1.exibir_mensagem()
        
#Exercicio 2
# class Pessoa:
#     def __init__(self,nome,idade):
#         self.nome= nome
#         self.idade=idade

#     def apresentar(self):
#         print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos')

# p1=Pessoa('joão', 25)
# p1.apresentar()

#Exercicio 3
# class Carro:
#     def __init__(self,marca,modelo,ano):
#         self.marca=marca
#         self.modelo=modelo
#         self.ano=ano
#     def exibir_mensagem(self):
#         print(f'Seu carro é {self.marca}, {self.modelo} de {self.ano}')
    
# carro1=Carro('Toyota','corola',2012)
# carro1.exibir_mensagem

#Exercicio 4 
#class Carro:
#     def __init__(self,marca,modelo,ano):
#         self.marca=marca
#         self.modelo=modelo
#         self.ano=ano
#     def exibir_mensagem(self):
#         print(f'Seu carro é {self.marca}, {self.modelo} de {self.ano}')
    
# carro1=Carro('Toyota','corola',2012)
# carro1.exibir_mensagem
# carro1=Carro('Honda', 'Civic g10', 2010)
# carro1.exibir_mensagem

#Exercicio 5
# class Conta_bancaria:
#     def __init__(self,titular, saldo=0,depositar=0):
#         self.titular=titular
#         self.saldo=saldo
#         self.depositar=depositar

#     def depositar(self,depositar=0):
#        print(f" seu saldo é : {self.depositar}") if depositar !=0 else (f'seu saldo é : -{self.depositar}')

# cliente=Conta_bancaria('Maria',0,250)
# cliente.depositar(250)
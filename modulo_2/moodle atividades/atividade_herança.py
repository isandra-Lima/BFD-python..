# ==========================
# Exercícios de Herança
# ==========================

# Exercício 1 - Criando a classe base Usuario
# Cria uma classe Usuario com atributos nome e email
# Inclui métodos para exibir informações e saudação
class Usuario:
    def __init__(self,nome,email):
        self.nome=nome
        self.email=email

    # Método para mostrar informações do usuário
    def exibir_informacoes(self):
        return f'Nome: {self.nome} - Email: {self.email}'
    
    # Método de saudação padrão
    def saudacao(self):
        return f'Olá, Usuario'
    
# Exercício 2 - Criando a classe Cliente que herda de Usuario
# Cria uma classe Cliente adiciona o atributo saldo e sobrescreve os métodos quando necessário    
class Cliente (Usuario):
    def __init__(self,nome,email,saldo):
       super().__init__(nome,email)   # Chama o construtor da classe pai para inicializar nome e email
       self.saldo=saldo

# Sobrescreve o método saudacao para personalizar para Cliente
    def saudacao(self):
        return f'Olá, Cliente'
    
    # Sobrescreve o método saudacao para personalizar para Cliente
    def exibir_informacoes(self):
        return f'{super().exibir_informacoes()}- Saldo: {self.saldo}'


# Criando um objeto Cliente e testando métodos   
cliente=Cliente('beatriz souza','beatriz@email.com','819981-6987',5000)
print(cliente)

print(cliente.exibir_informacoes())

print(cliente.saudacao())

#print(Usuario.saudacao(cliente)) #chamando o método da classe pai


# Exercício 3 - Criando a classe Funcionario que herda de Usuario
# Cria uma classe Funcionario adiciona o atributo telefone    
class funcionario(Usuario):
    def __init__(self,nome,email,telefone):
        super().__init__(nome,email)
        self.telefone=telefone
        
# Exercício 4 - Criando a classe Gerente que herda de Funcionario
# Cria uma classe Gerente adiciona o atributo cargo e sobrescreve exibir_informacoes

class Gerente(funcionario):
    def __init__(self,nome,email,telefone,cargo ):
        super().__init__(nome,email,telefone)
        self.cargo=cargo
    
    def exibir_informacoes(self):
        return f'{super().exibir_informacoes()} Telefone:{self.telefone}  - Cargo: {self.cargo}'

gerente=Gerente('Ana vitoria','anavi.@gmail.com','81874-596','gerente')
print(gerente.exibir_informacoes())

# Exercício 5 - Múltipla herança com Autenticacao e Permissao
# Cria uma classe Autenticacao cuida do login e status do usuário
class Autenticacao:
    def login(self,email,senha):
        self.email=email
        self.senha=senha
        return 'Você está logado no sistema'

    def status(self):
        return 'Usuário ativo no sistema'
    
# Cria uma classe Permissao cuida do nível de permissão e também tem status
class Permissao:
    def verificar_permissao(self,nivel):
        self.nivel=nivel
        return f'Permissão de {self.nivel} definida com sucesso'
    
    def status(self):
        return 'Permissão concedida'

# Exercício 6 - Criando a classe Administrador com múltipla herança
# Herda de Autenticacao e Permissao, podendo acessar métodos de ambas    
class Administrador(Autenticacao,Permissao):
    pass
    

administrador=Administrador()
print(administrador.login('ana12@gmail.com','1234'))
print(administrador.verificar_permissao('admin'))

# Qual status será chamado? depende da MRO 
administrador.status() 
# Mostrando a ordem de resolução de métodos (MRO)
print(Administrador.__mro__)

# O que é __mro__?

# __mro__ significa Method Resolution Order (Ordem de Resolução de Métodos).

# É uma tupla que mostra a ordem que o Python segue para procurar métodos quando você chama algo em uma classe que usa herança múltipla.

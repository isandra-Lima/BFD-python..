# ==========================
# Exercícios - Associação, Agregação e Composição
# ==========================

#==========================
# Exercício 1 - Associação
# Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.
# Uma Pessoa pode ter livros, mas Pessoa e Livro existem de forma independente.
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor  # Associação

pessoa=Pessoa("Alice")
livro=Livro("O massacre da familia hope","Riley Sager")
print(f"{pessoa.nome} está lendo '{livro.titulo}' de {livro.autor}.")

# ==========================
# Exercício 2 - Associação via método
# Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.
# Exemplo: o aluno pode pegar um ônibus, mas ambos existem independentemente.
class Onibus:
    def __init__(self, linha):
        self.linha = linha

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def pegar_onibus(self, onibus):
        print(f"{self.nome} pegou o ônibus da linha {onibus.linha}")

onibus1 = Onibus("101")
aluno1 = Aluno("Hilton")
aluno1.pegar_onibus(onibus1)  # Associação via método

# ==========================
# Exercício 3 - Agregação
# Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.
# Departamento deve agregar funcionários já criados. 
# Se o Departamento for destruído, os funcionários continuam existindo.
class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        
class Departamento:
    def __init__(self, funcionario):
        self.funcionario = funcionario  # Agregação 

funcionario1 = Funcionario("Bruno")
funcionario2 = Funcionario("isaque")
departamento = Departamento([funcionario1,funcionario2])

for f in departamento.funcionario:
    print(f"Funcionário {f.nome} trabalha no departamento.")
        
# ==========================
# Exercício 4 - Agregação com Time e Jogador
# Crie as classes Time e Jogador. 
# Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.
class Jogador:
    def __init__(self, nome,posicao):
        self.nome = nome
        self.posicao = posicao
        
class Time:
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores  # Agregação

j1 = Jogador("Messi", "Atacante")
j2 = Jogador("Neuer", "Goleiro")
time = Time("Seleção", [j1, j2])
print(f"Time: {time.nome} tem os jogadores: {', '.join([j.nome for j in time.jogadores])}.") # join é um método de string que junta os elementos de uma lista em uma única string, separados por vírgulas.

# ==========================
# Exercício 5 - Composição
# Crie a classe Carro que possui um Motor.
# O Motor deve ser criado dentro do Carro.
# Se o Carro deixar de existir, o Motor também deixa de existir.
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # Composição

carro1 = Carro("Fusca", 50)
print(carro1.motor.potencia) 
del carro1  

# ==========================
# Exercício 6 - Composição com Casa e Cômodos
# Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.).
# Cada Comodo deve ser criado dentro da Casa.
class Comodo:
    def __init__(self, nome):
        self.nome = nome
class Casa:
    def __init__(self):
        self.sala=Comodo("Sala")
        self.cozinha=Comodo("Cozinha")
        self.quarto=Comodo("Quarto")
        self.banheiro=Comodo("Banheiro")

casa=Casa()
print(f"A casa tem os cômodos: {casa.sala.nome}, {casa.cozinha.nome}, {casa.quarto.nome} e {casa.banheiro.nome}.")
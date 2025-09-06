# ==========================
# Exercícios de Funções
# ==========================

# ==== Exercício 1 ====
# Função de saudação
# Cria uma função que imprime uma mensagem de boas-vindas
def saudacao():
    print("Olá, bem-vindo ao Python!")
saudacao()


# ==== Exercício 2 ====
# Função dobro
# Retorna o dobro do número recebido como parâmetro
def dobro(numero):
    return numero * 2
print(dobro(5))
print(dobro(10))
print(dobro(-3))


# ==== Exercício 3 ====
# Função soma
# Retorna a soma de dois números
def soma(a, b):
    return a + b
print(soma(10, 20))


# ==== Exercício 4 ====
# Função mensagem
# Função com parâmetro padrão que imprime uma saudação personalizada
def mensagem(nome="visitante"):
    print(f"Olá, {nome}!")
mensagem("Maria")
mensagem()


# ==== Exercício 5 ====
# Função operacoes
# Retorna soma, subtração e multiplicação de dois números
def operacoes(a, b):
    return a + b, a - b, a * b
s, sub, m = operacoes(10, 5)
print("Soma:", s)
print("Subtração:", sub)
print("Multiplicação:", m)


# ==== Exercício 6 ====
# Função média
# Recebe qualquer quantidade de números e calcula a média
def media(*numeros):
    return sum(numeros) / len(numeros) if numeros else 0
print("Média de 3 valores:", media(10, 20, 30))
print("Média de 5 valores:", media(5, 10, 15, 20, 25))
print("Média de 7 valores:", media(1, 2, 3, 4, 5, 6, 7))


# ==== Exercício 7 ====
# Função dados_pessoais
# Recebe qualquer número de argumentos nomeados e imprime cada par chave-valor
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")
dados_pessoais(nome="Ana", idade=25, cidade="Recife")
print()
dados_pessoais(nome="João", idade=30, cidade="São Paulo", profissão="Engenheiro")


# ==== Exercício 8 ==== 
# Função calculadora (Opção 1)
# Calculadora usando funções internas para operações básicas
def calculadora(a, b, operacao):
    def somar(x, y): return x + y
    def subtrair(x, y): return x - y
    def multiplicar(x, y): return x * y
    def dividir(x, y): return x / y if y != 0 else "Erro: divisão por zero"

    if operacao == "soma":
        return somar(a, b)
    elif operacao == "subtracao":
        return subtrair(a, b)
    elif operacao == "multiplicacao":
        return multiplicar(a, b)
    elif operacao == "divisao":
        return dividir(a, b)
    else:
        return "Operação inválida"

print(calculadora(10, 5, "soma"))
print(calculadora(10, 5, "subtracao"))
print(calculadora(10, 5, "multiplicacao"))
print(calculadora(10, 5, "divisao"))


# ==== Exercício 8 ==== 
# Função calculadora (Opção 2)
# Calculadora usando dicionário de lambdas (segunda versão)
def calculadora2(a, b, operacao):
    operacoes = {
        'soma': lambda x, y: x + y,
        'substrair': lambda x, y: x - y,
        'multiplicar': lambda x, y: x * y,
        'dividir': lambda x, y: x / y if y != 0 else "Erro: divisão por zero"
    }

    funcao = operacoes.get(operacao)
    if funcao:
        return funcao(a, b)
    else:
        print('Operação inválida')

print(calculadora2(10, 5, 'substrair'))
print(calculadora2(10, 5, 'soma'))
print(calculadora2(10, 5, 'multiplicar'))
print(calculadora2(10, 0, 'dividir'))
print(calculadora2(10, 5, 'modulo'))  # Teste operação inválida


# ==== Exercício 9 ====
# Função aplicar_operacao
# Recebe dois números e uma função como parâmetro, aplicando a função a eles
def aplicar_operacao(a, b, funcao):
    return funcao(a, b)

def soma_op(a, b):
   return a + b

def multiplica_op(a, b):
    return a * b

print(aplicar_operacao(3, 4, soma_op))
print(aplicar_operacao(3, 4, multiplica_op))

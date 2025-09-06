# Funções

# Função é um bloco de código que realiza uma tarefa específica e pode ser reutilizado.

# Criar função:
# def nome_da_funcao(parametros):
#     # bloco de código
#     return valor  # opcional

# Exemplo:
# def soma(a, b):
#     return a + b

# Chamar função:
# resultado = soma(3, 5)
# print(resultado)  # imprime 8

# Parâmetros:
# - Podem ter valores padrão: def saudacao(nome="Usuário")
# - Podem ser posicionais ou nomeados

# Return:
# - Retorna um valor da função
# - Se não houver return, a função retorna None

# Funções podem ser usadas para organizar código, reduzir repetição e facilitar manutenção.

# ==========================
# global e local
# ==========================

# Variáveis locais: criadas dentro de funções, só existem lá.
# Variáveis globais: criadas fora, podem ser usadas em qualquer lugar.

# Para alterar uma global dentro da função, usar 'global':
# x = 5
# def mudar():
#     global x
#     x = 10
# mudar()
# print(x)  # 10

# Sem 'global', a atribuição cria uma variável local com o mesmo nome.

# ==========================
# Exercícios - Funções- sala
# ==========================

# Exercício 1: Função que soma dois números
# Crie uma função chamada soma que receba dois números como parâmetro e retorne a soma.
def soma(a, b):
    return a + b

print("Soma:", soma(3, 5))


# Exercício 2: Função que verifica se um número é par
# Crie uma função chamada eh_par que recebe um número e retorna True se for par, False se for ímpar.
def eh_par(n):
    return n % 2 == 0

print("O número 4 é par?", eh_par(4))
print("O número 7 é par?", eh_par(7))


# Exercício 3: Função com valor padrão
# Crie uma função chamada saudacao que receba um nome. Se não for informado, use "Usuário".
def saudacao(nome="Usuário"):
    print(f"Olá, {nome}!")

saudacao("Maria")
saudacao()  # usa valor padrão

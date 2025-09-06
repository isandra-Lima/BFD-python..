# FOR, IN e RANGE:
# O loop 'for' é usado para iterar sobre uma sequência (como lista, tupla, string, ou range).
# A palavra-chave 'in' indica que a variável irá percorrer cada elemento da sequência.
# A função 'range()' gera uma sequência de números, útil para controlar quantas vezes o loop vai executar.
# Exemplo: 
# for i in range(5):   # i vai assumir os valores 0, 1, 2, 3 e 4
#     print(i)


# ==========================
# Exercícios de repetição - FOR -sala
# ==========================

# Exercício 1: Imprimir números de 1 a 10
for i in range(1, 11):
    print(i)

# Exercício 2: Somar números de 1 a 50
soma = 0
for i in range(1, 51):
    soma += i
print("Soma de 1 a 50:", soma)

# Exercício 3: Imprimir elementos de uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)



# ==========================
# WHILE:
# O loop 'while' repete um bloco de código enquanto uma condição for verdadeira.
# É útil quando não sabemos exatamente quantas vezes o código deve rodar, mas dependemos de uma condição.
# Exemplo:
# x = 0
# while x < 5:       # executa enquanto x for menor que 5
#     print(x)
#     x += 1

# ==========================
# Exercícios de repetição - WHILE - sala
# ==========================

# Exercício 1: Contar de 1 a 5
x = 1
while x <= 5:
    print(x)
    x += 1

# Exercício 2: Somar números até o usuário digitar 0
total = 0
numero = int(input("Digite um número (0 para sair): "))
while numero != 0:
    total += numero
    numero = int(input("Digite outro número (0 para sair): "))
print("Soma total:", total)

# Exercício 3: Adivinhar a senha
senha_correta = "1234"
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")

print("Acesso permitido!")




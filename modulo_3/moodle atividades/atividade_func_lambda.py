# ==========================
# Exercícios - Funções Lambda- Map, Filter, Reduce e Sorted
# ==========================

# Exercício 1 - Usando map() com lambda
# Aplica uma função lambda a cada elemento da lista para dobrar os valores
numeros = [1, 2, 3, 4, 5]
dobro=list(map(lambda x: x*2, numeros))
print(dobro)

# Exercício 2 - Usando filter() com lambda
# Filtra apenas os números pares de uma lista
numero =[10, 15, 20, 25, 30]
pares=list(filter(lambda x: x%2==0, numero))
print(f"Os numeros pares são : {pares}")

# Exercício 3 - Usando reduce() com lambda
# Reduz (soma) todos os elementos da lista a um único valor
from functools import reduce
numero = [1, 2, 3, 4, 5]
soma = (reduce(lambda x, y: x + y, numero))
print(f"A soma dos numeros é : {soma}")

# Exercício 4 - Usando sorted() com lambda
# Ordena uma lista de frutas pelo tamanho da palavra (quantidade de letras)
frutas =  ["uva", "banana", "maçã", "laranja"]
ordenadas=sorted(frutas, key=lambda x: len(x))
print(f"As frutas ordenadas pelo tamanho são : {ordenadas}")

# Exercício 5 - Usando map() para capitalizar nomes
# Deixa apenas a primeira letra de cada nome maiúscula
nome = ["Ana", "João", "Maria", "Pedro"]
maiusculas= list(map((lambda x : x.capitalize()), nome))
print(f"Nomes: {maiusculas}")

# Exercício 6 - Usando reduce() para multiplicar todos os números
# Multiplica todos os elementos da lista usando reduce
from functools import reduce
numeros =  [2, 3, 4, 5]
multiplicaca=reduce(lambda x , y : x* y ,numeros)
print(f"A multiplicação dos numeros é : {multiplicaca}")

# Exercício 7 - Usando sorted() para ordenar pelo último caractere
# Ordena a lista de frutas considerando o último caractere de cada palavra
frutas = ["banana", "uva", "maçã", "laranja"]
ordenadas = sorted(frutas, key=lambda x :x[-1])
print(f"As frutas ordenadas pelo ultimo caractere são : {ordenadas}")
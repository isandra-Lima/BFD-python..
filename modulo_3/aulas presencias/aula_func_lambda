# ==========================
# Função Lambda
# ==========================
# Lambda é uma função anônima (sem nome), usada para tarefas simples e rápidas.
# É escrita em uma única linha, sem precisar usar 'def'.
#
# Sintaxe:
# lambda parametros: expressão
#
# Exemplo:
# dobro = lambda x: x * 2
# print(dobro(5))  # 10
#
# Também pode ser usada direto dentro de outras funções:
# print(list(map(lambda x: x * 2, [1, 2, 3])))  # [2, 4, 6]
#
# Lambdas são úteis quando precisamos de uma função pequena e temporária.

# ==========================
# Função map()
# ==========================
# Aplica uma função (como uma lambda) a cada item de uma lista ou sequência.
# Retorna um iterável com os resultados transformados.
#
# Sintaxe:
# map(funcao, iteravel)
#
# Exemplo:
# numeros = [1, 2, 3, 4]
# dobrados = list(map(lambda x: x * 2, numeros))
# print(dobrados)  # [2, 4, 6, 8]
#
# Uso: transformar todos os elementos de uma coleção.

# ==========================
# Função filter()
# ==========================
# Filtra os elementos de uma lista, mantendo apenas os que passam em um teste lógico.
# A função usada deve retornar True ou False.
#
# Sintaxe:
# filter(funcao, iteravel)
#
# Exemplo:
# numeros = [1, 2, 3, 4, 5, 6]
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)  # [2, 4, 6]
#
# Uso: selecionar itens que satisfazem uma condição.

# ==========================
# Função reduce()
# ==========================
# Reduz uma lista a um único valor, aplicando uma função cumulativa.
# É necessário importar de functools.
#
# Sintaxe:
# from functools import reduce
# reduce(funcao, iteravel)
#
# Exemplo:
# from functools import reduce
# numeros = [1, 2, 3, 4]
# soma = reduce(lambda x, y: x + y, numeros)
# print(soma)  # 10
#
# Uso: combinar todos os valores de uma sequência em um só (soma, produto etc.).

# ==========================
# Função sorted()
# ==========================
# Ordena os elementos de uma lista.
# Pode usar 'key' com lambda para definir o critério de ordenação.
#
# Sintaxe:
# sorted(iteravel, key=funcao, reverse=False)
#
# Exemplo:
# nomes = ["Ana", "joao", "Carlos", "beatriz"]
# ordenado = sorted(nomes, key=lambda nome: nome.lower())
# print(ordenado)  # ['Ana', 'beatriz', 'Carlos', 'joao']
#
# Uso: ordenar listas com base em uma regra personalizada.

# ==========================
# RESUMO FINAL
# ==========================
# lambda → cria funções rápidas e anônimas
# map() → transforma cada elemento
# filter() → escolhe apenas os que passam no teste
# reduce() → junta tudo em um único resultado
# sorted() → ordena conforme uma regra definida


# ==========================
# Exercícios - Função Lambda - sala
# ==========================

# Exercício 1: Lambda para cálculo simples
# Crie uma função lambda que receba dois números e retorne a soma deles.
# Em seguida, teste a função com diferentes valores.
soma = lambda a, b: a + b

print("Soma 1 + 2 =", soma(1, 2))
print("Soma 10 + 5 =", soma(10, 5))
print("Soma -3 + 7 =", soma(-3, 7))


# Exercício 2: Lambda com map()
# Dada uma lista de números, use map() e uma função lambda para dobrar cada valor da lista.
numeros = [2, 4, 6, 8, 10]
dobrados = list(map(lambda x: x * 2, numeros))
print("\nLista original:", numeros)
print("Lista dobrada:", dobrados)


# Exercício 3: Lambda com filter()
# Dada uma lista de idades, use filter() e uma função lambda para filtrar apenas as idades maiores ou iguais a 18.
idades = [12, 17, 18, 25, 30, 15, 40]
maiores = list(filter(lambda idade: idade >= 18, idades))
print("\nIdades originais:", idades)
print("Idades maiores de 18:", maiores)

#listas

#metodos 
# adição = list.insert (ordem,elemento) or list.append(elemento) or list.extend (varios elementos)
# remoção= list.remove(elemento) or list.pop(tanto pela ordem ou o ultimo)
#contagem= list.count( elemento)
#remoção de qualquer varialvel= del variavel, na lista del fruta[ordem]
#copia= list2=list[:]   or list.copy
#ordem= list.sort (ordem alfabetica) or list.reverse(ordena de qualquer jeito) or sorted.list

# ==========================
# Exercícios com listas - sala
# ==========================

# Exercício 1: Criar e imprimir uma lista
lista = ['amora', 23, 'morango', 25, 'banana', 5]
print(lista)


# Exercício 2: Inserir e remover elementos da lista
lista = ['amora', 23, 'morango', 25, 'banana', 5]
print("Lista original:", lista)

lista.insert(4, 'uva')  # Insere 'uva' na posição 4
print("Após inserir 'uva':", lista)

lista.remove('banana')   # Remove 'banana'
print("Após remover 'banana':", lista)


# Exercício 3: Copiar lista e mostrar IDs
lista = ['amora', 23, 'morango', 25, 'banana', 5]
lista2 = lista.copy()  # Corrigido para usar parênteses
print("ID da lista original:", id(lista))
print("ID da lista2 (cópia):", id(lista2))


# Exercício 4: Criar nova lista usando list comprehension
lista = [2, 5, 15, 30]
lista2 = [x * 5 for x in lista]
print(f"Lista original: {lista}")
print(f"Lista multiplicada por 5: {lista2}")


# Exercício 5: Fatiamento de listas
lista = [1, 2, 3, 4, 5, 6]
lista2 = lista[3:5]  # Pega do índice 3 até 4 (5 não incluído)
print(f"Sua nova lista (fatiada): {lista2}")

# Criar uma lista usando list comprehension com range
matriz = [i for i in range(4)]  # Gera [0, 1, 2, 3]
print("Lista com range:", matriz)

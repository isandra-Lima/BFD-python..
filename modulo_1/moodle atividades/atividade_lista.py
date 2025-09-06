# ==========================
# Exercícios de Lista
# ==========================

# Exercício 1 - Criando a lista de livros
# Cria uma lista com alguns livros e imprime
livros = ["Nunca minta", "A empregada", "Verity"]
print(f"Lista de livros:{livros}")

# Exercício 2 - Exibir o primeiro e o último elemento
# Mostra o primeiro e último livro da lista
print(f"Primeiro livro: {livros[0]}")
print(f"Ultimo livro:{livros[-1]}")

# Exercício 3 - Adicionar mais dois livros com append()
# Adiciona novos livros ao final da lista
livros.append("Não confie em ninguém")
livros.append("Procure nas cinzas")
print(f"Lista atualizada:{livros}")

# Exercício 4 - Inserir o livro "Duna" na segunda posição (índice 1)
# Insere o livro "Duna" no índice 1 da lista
livros.insert(1, "Duna")
print(f"Lista com Duna:{livros}")

# Exercício 5 - Remover "Silêncio dos inocentes" (com verificação)
# Remove um livro se ele existir na lista, senão mostra mensagem
if "Silêncio dos inocentes" in livros:
     livros.remove("Silêncio dos inocentes")
else:
     print("Livro não encontrado")
print(f"Lista final: {livros}")

# Exercício 6 - Criando a lista números
# Conta quantas vezes o número 2 aparece na lista
numeros = [1, 2, 3, 2, 4, 2, 5]
print(f"Quantidade de vezes que 2 aparece: {numeros.count(2)}")

# Exercício 7 - Percorrer a lista livros
# Imprime uma mensagem para cada livro da lista
for livro in livros:
    print(f"O livro {livro} é interessante")

# Exercício 8 - Exibir somente idades >= 18
# Percorre lista de idades e mostra somente as maiores ou iguais a 18
idades = [12, 18, 25, 14, 30]
for idade in idades:
    if idade >= 18:
      print(f"Idade maior ou igual a 18: {idade}")

# Exercício 9 - Soma manual dos valores
# Soma todos os valores de uma lista usando loop
valores = [10, 20, 30, 40]
soma = 0
for v in valores:
   soma += v
print(f"Soma dos valores: {soma}")

# Exercício 10 - Receber notas de 2 alunos e calcular média
# Pede 3 notas para cada aluno, calcula e mostra a média
notas = []
for i in range(2):
    aluno_notas = []
    print(f"Digite as 3 notas do aluno {i+1}:")
    for j in range(3):
         nota = float(input(f"Nota {j+1}: "))
         aluno_notas.append(nota)
         notas.append(aluno_notas)

for i, aluno in enumerate(notas):
     media = sum(aluno) / len(aluno)
     print(f"Média do aluno {i+1}: {media:.2f}")

# Exercício 11 - Criar tabuleiro de xadrez
# Cria um tabuleiro 8x8 usando listas e posiciona as peças iniciais
import numpy as np

# Tabuleiro vazio
tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]

# Peças pretas (linha 0 e 1)
tabuleiro[0] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
tabuleiro[1] = ["pea"] * 8

# Peças brancas (linha 6 e 7)
tabuleiro[6] = ["pea"] * 8
tabuleiro[7] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]

print("\nTabuleiro de Xadrez:")
print(np.array(tabuleiro))

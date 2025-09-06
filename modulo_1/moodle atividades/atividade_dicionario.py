# ==========================
# Exercícios de Dicionário
# ==========================

# Exercício 1 - Criar um dicionário simples
# Cria um dicionário com informações de um aluno e imprime
aluno = {
    "nome": "isandra",
    "idade": 19,
    "nota": 9
}
print(aluno)


# Exercício 2 - Acessando valores
# Mostra valores específicos de um dicionário de produto
produto = {
    "nome": "macarrão",
    "preço": 1.50,
    "estoque": 100
}
print(f"produto:{produto['nome']} e a quantidade em estoque:{produto['estoque']}")


# Exercício 3 - Adicionando novos pares chave-valor
# Adiciona a chave 'cidade' no dicionário pessoa
pessoa = {"nome": "Carlos", "idade": 30}
pessoa['cidade'] = 'São Paulo'
print(pessoa)


# Exercício 4 - Removendo elementos
# Remove a chave 'ano' do dicionário carro
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
del carro['ano']


# Exercício 5 - Verificando existência de uma chave
# Verifica se a chave 'telefone' existe no dicionário
contato = {"nome": "Ana", "email": "ana@email.com"}
if "telefone" in contato:
    print("A chave telefone existe.")
else:
    print("A chave telefone NÃO existe.")


# Exercício 6 - Contando frequência de palavras
# Cria uma função que conta quantas vezes cada palavra aparece em uma lista
def contar_palavras(lista):
    frequencia = {}
    for palavra in lista:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
print(contar_palavras(palavras))


# Exercício 7 - Invertendo chaves e valores de um dicionário
# Troca as chaves pelos valores e vice-versa
d = {"a": 1, "b": 2, "c": 3}
invertido = {}
for item in d:
    invertido[d[item]] = item
print(invertido)


# Exercício 8 - Dicionário com listas
# Calcula a média das notas de cada aluno em um dicionário
aluno = {
    "lucas": [7, 8, 6],
    "ana": [9, 8, 5],
    "pedro": [6, 7, 6]
}
for nome in aluno:
    media = sum(aluno[nome]) / len(aluno[nome])
    print(f"{nome} -> média:{media:.2f}")


# Exercício 9 - Mesclando dois dicionários
# Cria uma cópia de d1 e atualiza com os valores de d2
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
novo = d1.copy()
novo.update(d2)
print(novo)


# Exercício 10 - Ordenando dicionário por valores
# Ordena o dicionário pelo valor do maior para o menor
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
ordenados = sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True)
for nome, pontuacao in ordenados:
    print(nome, "->", pontuacao)

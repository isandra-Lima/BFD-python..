
# Dicionários

# Um dicionário é uma coleção de pares chave-valor.
# Cada chave é única e permite acessar o valor correspondente.
# Dicionários são úteis quando queremos associar informações.

# Criar dicionário:
# pessoa = {"nome": "João", "idade": 25, "cidade": "Fortaleza"}

# Acessar valores:
# pessoa["nome"]      -> retorna "João"
# pessoa.get("idade") -> retorna 25

# Adicionar ou atualizar valores:
# pessoa["profissao"] = "Engenheiro"  # adiciona nova chave
# pessoa["idade"] = 26                # atualiza valor existente

# Remover valores:
# del pessoa["cidade"]      # remove a chave 'cidade'
# pessoa.pop("idade")       # remove e retorna o valor de 'idade'

# Iterar sobre dicionário:
# for chave, valor in pessoa.items():
#     print(chave, valor)

# Obter só chaves ou só valores:
# pessoa.keys()   -> lista de chaves
# pessoa.values() -> lista de valores

# Copiar dicionário:
# pessoa2 = pessoa.copy()  # cria uma cópia independente

# ==========================
# Exercícios com Dicionários
# ==========================

# Exercício 1: Criar e imprimir um dicionário
pessoa = {"nome": "João", "idade": 25, "cidade": "Fortaleza"}
print("Dicionário:", pessoa)


# Exercício 2: Adicionar e remover itens do dicionário
pessoa = {"nome": "João", "idade": 25, "cidade": "Fortaleza"}
print("Dicionário original:", pessoa)

pessoa["profissao"] = "Engenheiro"  # Adiciona nova chave-valor
print("Após adicionar 'profissao':", pessoa)

del pessoa["idade"]  # Remove a chave 'idade'
print("Após remover 'idade':", pessoa)


# Exercício 3: Acessar valores do dicionário
pessoa = {"nome": "João", "idade": 25, "cidade": "Fortaleza"}
print("Nome da pessoa:", pessoa["nome"])
print("Cidade da pessoa:", pessoa.get("cidade"))  # Outra forma de acessar


# Exercício 4: Iterar sobre chaves e valores
pessoa = {"nome": "João", "idade": 25, "cidade": "Fortaleza"}
for chave, valor in pessoa.items():  # items() retorna chave e valor
    print(f"{chave}: {valor}")


# Exercício 5: Criar dicionário a partir de duas listas
chaves = ["nome", "idade", "cidade"]
valores = ["Maria", 30, "São Paulo"]
dicionario = dict(zip(chaves, valores))  # zip combina as listas
print("Dicionário criado a partir de listas:", dicionario)

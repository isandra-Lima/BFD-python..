# POO - Associação, Agregação e Composição
# ==========================

# ==========================
# Associação
# ==========================
# Associação é um relacionamento entre classes onde uma conhece a outra, 
# mas ambas podem existir de forma independente.
# Exemplo: Um Professor e uma Disciplina. 
# Um professor pode existir sem a disciplina, e uma disciplina pode existir sem o professor.

# class Professor:
#     pass
#
# class Disciplina:
#     def __init__(self, professor):
#         self.professor = professor  # Associação

# ==========================
# Agregação
# ==========================
# Agregação é uma forma mais forte de associação. 
# Um objeto "tem um" outro objeto, mas o objeto contido pode existir sozinho.
# Exemplo: Um Departamento tem Professores. 
# Se o Departamento for destruído, os Professores ainda existem.

# class Departamento:
#     def __init__(self, professores):
#         self.professores = professores  # Agregação

# ==========================
# Composição
# ==========================
# Composição é um relacionamento forte onde o objeto "é parte de" outro.
# Se o objeto “todo” for destruído, as partes também são destruídas.
# Exemplo: Um Carro tem um Motor. 
# Se o Carro for destruído, o Motor também deixa de existir.

# class Motor:
#     pass
#
# class Carro:
#     def __init__(self):
#         self.motor = Motor()  # Composição

# ==========================
# RESUMO FINAL
# ==========================
# Associação → conhece, mas existe independente.
# Agregação → "tem um", mas parte pode existir sozinha.
# Composição → "é parte de", parte não existe sem o todo.

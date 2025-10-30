import sqlite3

conect=sqlite3.connect('escola_v2.db')
cursor=conect.cursor()

#2.Faça a query para pegar toda a tabela alunos e imprima na tela.
print("------Tabela Alunos------")
cursor.execute("SELECT * FROM Aluno")
for linha in cursor.fetchall():
    print(linha)

#3.Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas os 10 maiores notas. No fim imprima na tela a lista desses alunos e suas médias.
print("\n------Tabela Alunos------")
cursor.execute("""
select nome, (nota1 + nota2)/ 2.0 as media 
               from Aluno
               order by media desc
               limit 10;
               """)
top_10= cursor.fetchall()
for nome, media in top_10:
    print(f'Aluno: {nome} - Média: {media:.2f}')

#4.Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
print("\n------Tabela Alunos com Turmas------")
cursor.execute("""
select a.id, a.nome, a.nota1, a.nota2, t.id
         from Aluno a
         left join Turma t
         on a.id_turma = t.id;
         """)
for linha in  cursor.fetchall():
    print(f"id Aluno: {linha[0]} - Nome: {linha[1]} - Nota1: {linha[2]} - Nota2: {linha[3]} - id Turma: {linha[4]}")

#5Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.
print("\n------Tabela Alunos da Turma 2------")
cursor.execute("""
select a.id, a.nome, a.nota1, a.nota2, t.id
          from Aluno a
         left join Turma t
        on a.id_turma = t.id
        where t.id = 2
        """)
for linha in  cursor.fetchall():
    print(f"id Aluno: {linha[0]} - Nome: {linha[1]} - Nota1: {linha[2]} - Nota2: {linha[3]} - id Turma: {linha[4]}")

conect.close()

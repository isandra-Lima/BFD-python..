# ==========================
# Exercícios - SQL
# ==========================

--1.COUNT Mostre quantos alunos estão cadastrados na tabela Aluno. (Use a função COUNT)
select count(*) as total_alunos from aluno;

--2.MIN Mostre a menor mensalidade entre todos os cursos cadastrados. (Use a função MIN)
select min(mensalidade) as menor_mensalidade from curso;

--3.MAX Mostre a maior nota1 registrada entre todos os alunos. (Use a função MAX)
select max(nota1) as maior_nota1 from aluno;

--4.SUM Calcule o valor total das mensalidades de todos os cursos. (Use a função SUM)
select sum(mensalidade) as total_mensalidades from curso;

--5.AVG Mostre a média geral da nota2 dos alunos. (Use a função AVG)
select round(avg(nota2),2) as media_nota2 from aluno;
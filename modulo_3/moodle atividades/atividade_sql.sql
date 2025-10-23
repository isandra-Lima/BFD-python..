# ==========================
# Exercícios - SQL
# ==========================


-- 1. Mostre todos os registros da tabela Aluno
select * from aluno;

-- 2. Exiba apenas o nome e a nota1 de todos os alunos
select nome, nota1 from aluno;

 --3.Liste todos os alunos cuja nota2 seja maior que 8
select * from aluno where nota2 > 8;

--4.Mostre os alunos que nasceram após o ano de 2000
select * from aluno where data_nascimento > '2000-12-31';

--5.Exiba o nome e a mensalidade de todos os cursos que custam mais de 600 reais.
select nome, mensalidade from curso where mensalidade > 600;

--6.Mostre o nome das turmas e o ano correspondente, ordenados pelo ano em ordem crescente
select nome, ano from turma order by ano asc;

--7. Liste o ano das turmas e a quantidade de turmas por ano. 
select ano, count(*) as quantidade_turmas from turma group by ano;

--8.Calcule a média da nota1 dos alunos por turma_id.
select id_turma, round(avg(nota1),2) as media_nota1 from aluno group by id_turma;

--9.Mostre o ano e a quantidade de turmas apenas para os anos que têm mais de 2 turmas
select ano, count(*) as quantidade_turmas from turma group by ano having count(*) > 2;

--10.Exiba o nome dos cursos e suas mensalidades, ordenando primeiro pela mensalidade
select nome, mensalidade from curso order by mensalidade desc;
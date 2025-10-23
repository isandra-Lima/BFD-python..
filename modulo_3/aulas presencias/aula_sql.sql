# ==========================
# COMANDOS SQL - RESUMO COMPLETO
# ==========================
# Este arquivo explica os principais comandos SQL utilizados
# para consultar, filtrar, agrupar e ordenar dados em um banco.
# Inclui exemplos práticos e comentários didáticos.

# ==========================
# Comando SELECT
# ==========================
# O comando SELECT é usado para buscar dados de uma tabela no banco de dados.
# Pode exibir todas as colunas (*) ou apenas as que forem especificadas.
#
# Sintaxe:
# SELECT colunas FROM tabela;
#
# Exemplos:
select * from aluno;                -- mostra todas as colunas e registros
select nome, nota1 from aluno;      -- mostra apenas as colunas nome e nota1
#
# Uso: visualizar dados armazenados nas tabelas.

# ==========================
# Cláusula WHERE
# ==========================
# Filtra os resultados com base em uma condição.
# Mostra apenas os registros que atendem ao critério informado.
#
# Sintaxe:
# SELECT colunas FROM tabela WHERE condição;
#
# Exemplos:
select * from aluno where nota2 > 8;  
select * from aluno where data_nascimento > '2000-12-31';
#
# Uso: buscar registros específicos dentro de uma tabela.

# ==========================
# ORDER BY
# ==========================
# Define a ordem de exibição dos resultados (crescente ou decrescente).
#
# Sintaxe:
# SELECT colunas FROM tabela ORDER BY coluna [ASC|DESC];
#
# Exemplos:
select nome, ano from turma order by ano asc;   -- ordem crescente
select nome, mensalidade from curso order by mensalidade desc; -- ordem decrescente
#
# Uso: organizar os resultados de forma ordenada.

# ==========================
# Função COUNT() e GROUP BY
# ==========================
# COUNT() conta o número de registros.
# GROUP BY agrupa registros com base em uma ou mais colunas.
#
# Sintaxe:
# SELECT coluna, COUNT(*) FROM tabela GROUP BY coluna;
#
# Exemplo:
select ano, count(*) as quantidade_turmas from turma group by ano;
#
# Uso: agrupar dados e contar quantos registros existem em cada grupo.

# ==========================
# Funções Agregadas e ROUND()
# ==========================
# AVG() calcula a média, SUM() soma, MIN() e MAX() pegam o menor e maior valor.
# ROUND() arredonda números.
#
# Sintaxe:
# SELECT coluna, ROUND(AVG(coluna), 2) FROM tabela GROUP BY coluna;
#
# Exemplo:
select id_turma, round(avg(nota1),2) as media_nota1 from aluno group by id_turma;
#
# Uso: realizar cálculos sobre conjuntos de dados.

# ==========================
# HAVING
# ==========================
# Semelhante ao WHERE, mas usado para filtrar resultados depois do GROUP BY.
#
# Sintaxe:
# SELECT coluna, COUNT(*) FROM tabela GROUP BY coluna HAVING condição;
#
# Exemplo:
select ano, count(*) as quantidade_turmas 
from turma 
group by ano 
having count(*) > 2;
#
# Uso: exibir apenas grupos que atendem a uma condição.



# ==========================
# RESUMO FINAL
# ==========================
# SELECT → exibe os dados
# WHERE → filtra os resultados
# ORDER BY → ordena as informações
# GROUP BY → agrupa registros
# COUNT(), AVG(), ROUND() → realizam cálculos
# HAVING → filtra resultados agrupados
#
# Exemplo completo combinando vários comandos:
# select ano, count(*) as quantidade
# from turma
# group by ano
# having count(*) > 2
# order by ano asc;

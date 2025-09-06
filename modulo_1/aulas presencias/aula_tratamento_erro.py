# Tratamento de Erros

# Em Python, podemos tratar erros usando try/except para evitar que o programa quebre.

# try: bloco de código que pode gerar erro
# except: bloco que trata o erro específico ou genérico
# finally: bloco que sempre é executado, independentemente de ocorrer erro ou não
# raise: serve para lançar um erro manualmente

# Exemplo:
# try:
#     x = int(input("Digite um número: "))
#     print(10 / x)
# except ValueError:
#     print("Erro: valor inválido!")
# except ZeroDivisionError:
#     print("Erro: divisão por zero!")
# finally:
#     print("Fim do programa.")
# raise ValueError("Erro manual!")  # força o erro


# ==========================
# Exercícios - Tratamento de Erros - sala
# ==========================

# Exercício 1: Tratar ValueError
# Peça ao usuário um número inteiro. Se ele digitar algo que não seja número, trate o erro.
try:
    num = int(input("Digite um número inteiro: "))
    print("Você digitou:", num)
except ValueError:
    print("Erro: você não digitou um número inteiro!")


# Exercício 2: Tratar divisão por zero com finally
# Peça dois números e divida o primeiro pelo segundo. Sempre mostre "Fim do programa".
try:
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o denominador: "))
    resultado = a / b
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero!")
else:
    print("Resultado:", resultado)
finally:
    print("Fim do programa.")


# Exercício 3: Usar raise para lançar um erro manualmente
# Crie uma função que recebe um número. Se o número for negativo, lance um ValueError.
def verificar_positivo(n):
    if n < 0:
        raise ValueError("Número negativo não permitido!")
    else:
        print("Número válido:", n)

verificar_positivo(5)
# verificar_positivo(-3)  # Vai lançar ValueError


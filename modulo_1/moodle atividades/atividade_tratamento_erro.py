# ==========================
# Exercícios de Tratamento de Erro
# ==========================

# ==== Exercício 1 ====
# Tratar ValueError
# Peça ao usuário um número inteiro. Se ele digitar algo que não seja número, trate o erro.
try:
    num = int(input('Digite um numero inteiro: '))
    print(f'Você digitou o número {num}')
except:
    print('Você não digitou um número inteiro')


# ==== Exercício 2 ====
# Tratar ValueError em uma multiplicação
# Peça dois números inteiros ao usuário e calcule a multiplicação. Trate o erro se não forem inteiros.
try:
    num1 = int(input('Digite um numero inteiro: '))
    num2 = int(input('Digite um numero inteiro: '))
    mut = num1 * num2
    print(f'O resultado de {num1} x {num2} é: {mut}')
except:
    print('Você não digitou um número inteiro')


# ==== Exercício 3 ====
# Usando try e else
# Peça um número inteiro. Se o usuário digitar corretamente, execute o bloco else.
try:
    num1 = int(input('Digite um numero inteiro: '))
except:
    print('Você não digitou um número inteiro')
else:
    print(f'Você digitou o número {num1}')


# ==== Exercício 4 ====
# Tratamento de arquivo com try/except/finally
# Tenta abrir um arquivo. Se não existir, exibe mensagem. Sempre exibe encerramento.
import os
try:
    os.open('dados.txt')
    print(f'Seu arquivo foi encontrado')
except:
    print('Seu arquivo não foi encontrado')
finally:
    print('Encerrando programa')


# ==== Exercício 5 ====
# Usando raise
# Cria função que levanta erro se houver divisão por zero
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError('Divisão por zero não é permitido')
    return a / b

try:
    print(dividir(10, 2))
finally:
    print('Encerrando programa')


# ==== Exercício 6 ====
# Criando exceção personalizada
# Levanta um erro se idade for inválida
class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError('Idade não pode ser negativa')
    print(f'Idade cadastrada: {idade}')

# Exemplo de uso
try:
    cadastrar_idade(-5)
except IdadeInvalidaError as e:
    print(e)
finally:
    print('Encerrando programa')


# ==== Exercício 7 ====
# Tratamento de múltiplas exceções
# Peça dois números e divida. Trate ValueError e ZeroDivisionError
try:
    num1 = int(input('Digite um numero inteiro: '))
    num2 = int(input('Digite outro numero inteiro: '))
    resultado = num1 / num2
    print(f'O resultado de {num1} / {num2} é: {resultado}')
except ValueError:
    print('Você não digitou um número inteiro')
except ZeroDivisionError:
    print('Divisão por zero não é permitida')
finally:
    print('Encerrando programa')

# ==== Exercício 8 ====
# Verificar se número é par ou ímpar com tratamento de erro
try: 
    num1 = int(input('Digite um numero inteiro: ')) 
except ValueError:
     print('Você não digitou um número inteiro')
else :
     print(f'O número {num1} é par') if num1 % 2 == 0 else print(f'O número {num1} é ímpar')
finally:
    print('Encerrando programa')

# ==== Exercício 9 ====
# Simulando saque bancário com exceção personalizada

class SaldoInsuficienteError(Exception):
    pass
def sacar(saldo,valor):
    if valor > saldo:
        raise SaldoInsuficienteError('Saldo insuficiente para saque')
    return saldo - valor
try:
    saldo_atual = 1000
    valor_saque = float(input('Digite o valor para saque: '))
    novo_saldo = sacar(saldo_atual, valor_saque)
    print(f'Saque realizado com sucesso. Novo saldo: {novo_saldo}')
except SaldoInsuficienteError as e:
    print(F'ERROR:{e}')
finally:
    print('Encerrando programa')
    


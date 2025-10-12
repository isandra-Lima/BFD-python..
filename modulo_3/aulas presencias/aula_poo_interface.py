# ==========================
# Interface em POO 
# ==========================
# Interface é um “contrato” que define um conjunto de métodos que uma classe deve implementar.
# Serve para garantir que diferentes classes tenham o mesmo comportamento básico,
# mesmo que cada uma implemente à sua maneira.
#
# Python não tem uma palavra-chave "interface" como Java,
# mas podemos criá-las usando classes abstratas (ABC) com métodos abstratos.

# ==========================
# Criando uma Interface
# ==========================
# Uma interface é representada por uma classe abstrata que contém apenas métodos abstratos.

# from abc import ABC, abstractmethod
#
# class ControleRemoto(ABC):
#     @abstractmethod
#     def ligar(self):
#         pass
#
#     @abstractmethod
#     def desligar(self):
#         pass
#
# Nenhum método tem implementação — apenas a “assinatura” do que deve existir.

# ==========================
# Implementando uma Interface
# ==========================
# Uma classe que "implementa" a interface precisa obrigatoriamente definir todos os métodos dela.

# class TV(ControleRemoto):
#     def ligar(self):
#         print("TV ligada.")
#
#     def desligar(self):
#         print("TV desligada.")
#
# class ArCondicionado(ControleRemoto):
#     def ligar(self):
#         print("Ar-condicionado ligado.")
#
#     def desligar(self):
#         print("Ar-condicionado desligado.")
#
# controle_tv = TV()
# controle_tv.ligar()       # "TV ligada."
# controle_tv.desligar()    # "TV desligada."
#
# controle_ar = ArCondicionado()
# controle_ar.ligar()       # "Ar-condicionado ligado."
# controle_ar.desligar()    # "Ar-condicionado desligado."

# ==========================
# Regras Importantes
# ==========================
# 1. Não é possível instanciar uma interface diretamente.
#    Exemplo: ControleRemoto() → ERRO.
#
# 2. Todas as classes que herdam da interface DEVEM implementar todos os métodos abstratos.
#
# 3. Interfaces ajudam a manter o código padronizado e fácil de expandir.

# ==========================
# Vantagens do uso de Interfaces
# ==========================
# ✅ Garante consistência entre classes diferentes.
# ✅ Facilita manutenção e testes.
# ✅ Permite polimorfismo — diferentes objetos podem ser usados da mesma forma.
# ✅ Torna o código mais organizado e extensível.

# ==========================
# RESUMO FINAL
# ==========================
# Interface → contrato que define métodos obrigatórios.
# Criada com ABC + @abstractmethod.
# Serve para padronizar comportamentos entre classes.
# Classe que implementa → deve definir todos os métodos da interface.
# Interface = promessa de comportamento; classe concreta = cumprimento dessa promessa.

# ==========================
# Exercício - Interface em POO
# ==========================
# Crie uma interface chamada "Pagamento" com métodos abstratos:
# "pagar()" e "estornar()".
# Depois, crie duas classes: "CartaoCredito" e "Pix".
# Cada uma deve implementar os métodos de forma diferente.
#
# Dica: use from abc import ABC, abstractmethod

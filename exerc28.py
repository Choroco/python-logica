# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário 
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep

# n = random.randrange(0,5)
# valor = int(input("Tente adivinha o numero de 0 a 5 que a maquina escolheu: "))
# print("""O valor escolhido {}
# O valor que a maquina eslheu {}""".format(n, valor))
# if valor == n:
#   print("Parabens, Voce acertou!")
# else:
#   print("O computador venceu!")

computador = random.randint(0,5)
print("-=-"*20)
print("Pensei em um numero de 0 a 5... Tente adivinhar!")
print("-=-"*20)
jogador = int(input("Em que numero eu pensei? "))
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
  print("Voce ganhou!!!")
else:
  print("GANHEI! O nume que pensei foi {} e nao {}".format(computador, jogador))

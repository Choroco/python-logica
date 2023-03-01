# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
x = float(input("Digite um numero real qualquer para mostrar a sua porcao inteira: "))
#Arredonda
print("{:.0f}".format(x))
#Arredonda pra baixo
print(math.floor(x))
#Arredonda pra cima
print(math.ceil(x))
#Nao arredonda
print(math.trunc(x))
#Funciona como trunc
print(int(x))

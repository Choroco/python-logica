#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input("Digite o angulo para descobris seu seno, cosseno e tangente: "))

an = math.radians(ang)

print("O coseno de {} e: {:.2f}".format(ang, math.cos(an)))
print("O seno de {} e: {:.2f}".format(ang, math.sin(an)))
print("A tangente de {} e: {:.2f}".format(ang, math.tan(an)))

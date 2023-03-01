#Faça um programa que leia o comprimento do cateto oposto e do 
#cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

print("A hipotenusa tem o comprimento de: {:.2f}".format(math.hypot(co,ca)))


print(((co**2)+(ca**2))**(1/2))


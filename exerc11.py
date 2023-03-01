#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e 
#a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))

print("A area da parede é: {}m²\nSera necessario {}l de tinta.".format(altura*largura, (altura*largura)/2))

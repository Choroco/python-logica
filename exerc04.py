# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre 
# na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
print(40*"*-")

x = input("digite algo: ")

print(40*"*-")

print("Carecteristicas do valor digitado")
print("tipo: {}".format(type(x)))
print("É alnum: {}".format(x.isalnum()))
print("É alpha: {}".format(x.isalpha()))
print("É num: {}".format(x.isnumeric()))
print("É upper: {}".format(x.isupper()))
print("É ASCII: {}".format(x.isascii()))
print("É lower: {}".format(x.islower()))
print("É space: {}".format(x.isspace()))
print("É title: {}".format(x.istitle()))
#title contem maiúscula e minúscula 
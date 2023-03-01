# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
from os import system
system("cls")

cidade = str(input("Digite o nome de uma cidade: ")).strip().title()
cidade = cidade.split()

print("Santo" in cidade[0])

#Jeito do guanabas

cid = str(input("Digite on nome da cidade: ")).strip().title()
print(cid[:5] == "Santo")

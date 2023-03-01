# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

# Meu jeito
nome = input("Digite o seu nome completo: ")

print("Todas as letras minúsculas: {} \nTodas as letras maiúsculas: {}".format(nome.lower(), nome.upper()))
nomesspc = nome.replace(" ","")
print("O seu nome tem {} letras.".format(len(nomesspc)))
nomesplit = nome.split()
print("O seu primeiro nome '{}' tem {} letras.".format(nomesplit[0].title(),len(nomesplit[0])))

#=========================================================================================
# o do Guanabas
nome = str(input("Digite o seu nome completo: ")).strip()

# o primeiro e a mesma coisa
print("O seu nome tem {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" "))) 
# O problema e que se o usuario colocar so o primeiro nome da errado conta como inexistente

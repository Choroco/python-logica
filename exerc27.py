#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite o seu nome completo: ")).strip().title()
nome = nome.split()
print("""O seu primeiro nome e {}
O seu ultimo nome e {}""".format(nome[0],nome[len(nome)-1]))

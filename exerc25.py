#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input("Digite o seu nome: ")).strip().lower()
print("silva" in nome) #operador que o guanabas usou
nome = nome.find("silva")
print("O seu nome tem 'Silva'?",nome >= 0)


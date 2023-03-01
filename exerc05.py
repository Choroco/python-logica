#Faça um programa que leia um numero inteiro e mostre seu sucessor e antecessor
valor = int(input("Digite o número para descobrir seu antecessor e sucessor: "))
print("O antecessor de {0} é: {1}\nO sucessor de {0} é: {2}".format(valor, valor-1, valor+1))
#Desenvolva um programa que leia as duas notas de um aluno e calcule a sua média
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print("A media de {} e {} é: {:.1f}".format(nota1, nota2, (nota1+nota2)/2))

# Só pra testar, colocando a quantidade que quiser de notas

#lista = []
#soma = 0
#laco = True
#while laco:
#    lista.append(float(input("Digite o valor a comparar para tirar a média: ")))
#    quebra = input("Digite \"n\" para ver a média: ")
#    if quebra == "n":
#        laco = False
#quantidade = len(lista)
#for valorAtual in lista:
#    soma += valorAtual
#media = soma/quantidade
#print("A sua média é : {}".format(media))
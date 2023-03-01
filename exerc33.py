# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 > n2 and n1 > n3:
  maiorNumero = n1
elif n2 > n1 and n2 > n3:
  maiorNumero = n2
else:
  maiorNumero = n3

if n1 < n2 and n1 < n3:
  menorNumero = n1
elif n2 < n1 and n2 < n3:
  menorNumero = n2
else:
  menorNumero = n3

print("""O maior numero e {}
O menor numero e {}""".format(maiorNumero, menorNumero))

# jeito que eu pensei
# maiorNumero = 0
# lista = []
# for x in range(0,3):
#   lista.append(int(input("Digite o numero a comparar: ")))

# for numeroAtual in lista:
#   if numeroAtual > maiorNumero:
#     maiorNumero = numeroAtual

# menorNumero = maiorNumero

# for numeroAtual in lista:
#   if numeroAtual < menorNumero:
#     menorNumero = numeroAtual

# print("""O maior numero e {}
# O menor numero e {}""".format(maiorNumero, menorNumero))

# Exercício Python 23: Faça um programa que leia um 
# número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input("Digite um numero de 0 a 9999: "))
num = str(num)
num1 = str("{:>4}".format(num))
num1 = str(num1.replace(" ", "0"))
print("""O seu numero '{0}' tem:
{1} Milhar
{2} Centena
{3} Dezena
{4} Unidade""".format(num, num1[0], num1[1], num1[2], num1[3]))

#Forma que o guanabas fez
num = int(input("digite um numero: "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print("""O seu numero '{0}' tem:
{1} Milhar
{2} Centena
{3} Dezena
{4} Unidade""".format(num, milhar, centena, dezena, unidade))

#Crie um programa que leia um valor e mostre o seu dobro, triplo, raiz quadrada
valor = float(input("Digite o valor para calcular o dobro, triplo e sua raiz quadrada: "))
print("O dobro de {} é: {}".format(valor,valor*2))
print("O triplo de {} é:{}".format(valor, valor*3))
print("A raiz quadrada de {} é: {:.2f}".format(valor, valor**(1/2)))
#pow calcula potenciaçõa pow(2, 3) == 2**3                  ^
#                                                           |
#                                                           | 
#                                                  pow(valor, (1/2))
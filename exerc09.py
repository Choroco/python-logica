#Faça um progama que leia um valor e mostre a sua tabuada
valor = int(input("Digite um número: "))
print("="*20)
print("A tabuada de {} é: ".format(valor))
print("{} *  0 =".format(valor), valor*0)
print("{} *  1 =".format(valor), valor*1)
print("{} *  2 =".format(valor), valor*2)
print("{} *  3 =".format(valor), valor*3)
print("{} *  4 =".format(valor), valor*4)
print("{} *  5 =".format(valor), valor*5)
print("{} *  6 =".format(valor), valor*6)
print("{} *  7 =".format(valor), valor*7)
print("{} *  8 =".format(valor), valor*8)
print("{} *  9 =".format(valor), valor*9)
print("{} * 10 =".format(valor), valor*10)
print("="*20)
#Quis fazer do meu jeito

#valor = int(input("Digite um número: "))
#print("A tabuada de {} é:".format(valor))
#for x in range(0,11):
#        print("{}*{}= {}".format(valor, x, x*valor))
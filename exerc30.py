n = int(input("Digite um numero para descobrir se e pa ou impar: "))
n1 = n % 2
if n1 == 0:
  print("O numero {} e par".format(n))
else:
  print("O numero {} e impar".format(n))

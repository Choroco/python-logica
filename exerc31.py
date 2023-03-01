km = float(input("Qual a distancia em km sera percorrida: "))

if km <= 200:
  print("O valor da passagem ficara: R${:.2f}".format(km*0.50))
else:
  print("O valor da passagem ficara: R${:.2f}".format(km*0.45))

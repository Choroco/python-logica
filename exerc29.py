# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velo = float(input("Qual a velocidade do carro: "))
if velo > 80:
  print("""Voce ultrapassou 80 Km/h, tera que pagar R$ 7.00 por cada Km/h ultrapassado
Total: R$ {:.2f}""".format((velo - 80)*7))
else:
  print("Tenha um bom dia! Dirija com seguranca...")

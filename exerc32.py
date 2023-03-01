#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime

dataAtual = str(datetime.date.today())
dataAtual = dataAtual.replace("-"," ").split()
dataAtual = int(dataAtual[0])
# Toda essa gambiarra de cima pode ser substituida por:
# dataAtual = datetime.date.today().year
ano = int(input("Qual ano deseja analizar? Digite 0 para analizar o ano atual: "))

if ano == 0:
  ano = dataAtual

anoBi1 = ano % 4
anoBi2 = ano % 100
anoBi3 = ano % 400
if (anoBi1 == 0 and anoBi2 != 0) or (anoBi3 == 0 and anoBi2 == 0):
  print("O ano {} e um ano bissexto".format(ano))
else:
  print("O ano {} nao e um ano bissexto".format(ano))

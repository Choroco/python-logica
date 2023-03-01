#Escreva um programa que o valor convertido em metros e o exiba convertido em centimetro e milímetros
distancia = float(input("Digite uma distância em metros: "))
print("{}km".format(distancia/1000))
print("{}hm".format(distancia/100))
print("{}dam".format(distancia/10))
print("{}m".format(distancia))
print("{}dm".format(distancia*10))
print("A distância de {}m equivale a: {}cm".format(distancia, distancia*100))
print("A distância de {}m equivale a: {}mm".format(distancia, distancia*1000))

#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celcius = float(input("Qual a temperatura atual em °C? "))
print("A temperatura de {:.1f}°C convertida para °F ficara: {:.1f}°F".format(celcius, (celcius * 9 / 5) + 32))

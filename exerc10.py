#Crie um programa que leia quanto dinheiro 
#uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input("Quanto dinheiro você tem na carteira? R$ "))
print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(real, real/4.77))
print("Com R$ {:.2f} voce pode comprar EU$ {:.2f}".format(real, real/5.12))
print("Com R$ {:.2f} voce pode comprar JP$ {:.3f}".format(real, real/0.037))
print("Com R$ {:.2f} voce pode comprar BTC {:.7f}".format(real, real/147812.42))

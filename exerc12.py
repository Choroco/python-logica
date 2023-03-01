# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input("Digite o valo que sera dado desconto de 5%: R$"))
print("O valor de R${:.2f} com o desconto de 5%".format(preco),"ficara: R${:.2f}".format(preco*0.95))

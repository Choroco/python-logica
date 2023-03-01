#  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o seu salario atual: R$"))
print("O seu salario com o aumento de 15%","ficara: R${:.2f}".format(salario*1.15))

preco = float(input("Digite o valor atual do produto: R$"))
print("O valor a vista tera 7%","de desconto ficando: R${:.2f}".format(preco*0.93))
print("O valor parcelado tera um acrescimo de 8%","ficando: R${:.2f}".format(preco*1.08))

salario = float(input("Digite o salario para receber um aumento: R$"))

if salario <= 1250:
  print("O salario de R$ {:.2f} com o aumento de 15% ficara: R${:.2f}".format(salario, salario*1.15))
else:
  print("O salario de R$ {:.2f} com o aumento de 10% ficara: R${:.2f}".format(salario, salario*1.10))

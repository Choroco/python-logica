lado1 = float(input("\033[93mdigite o comprimento da primeira aresta: "))
lado2 = float(input("digite o comprimento da segunda aresta: "))
lado3 = float(input("digite o comprimento da terceira aresta: "))

if (lado2 - lado3) < lado1 and lado1 < (lado2 + lado3):
  print("\033[92mForma um trinagulo!")
else:
  print("\033[91mNao forma um triangulo!")

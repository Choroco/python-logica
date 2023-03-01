# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos 
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

al1 = input("Digite o nome do primeiro aluno: ")
al2 = input("Digite o nome do segundo aluno: ")
al3 = input("Digite o nome do terceito aluno: ") 
al4 = input("Digite o nome do quarto aluno: ")

print(random.sample([al1, al2, al3, al4], k=4))

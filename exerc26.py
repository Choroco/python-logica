#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input("Digite uma frase: ")).strip().lower()
frase = frase.split()
frase = " ".join(frase)
#print("""A sua frase tem {} letras 'a'
#A primeira letra 'a' esta no index {} e a ultima esta no {}""".format(fracom.count("a"),fracom.find("a"),fracom.rfind("a")))
print("""A sua frase tem {} letras 'a'
A primeira letra 'a' esta na posicao {}
A ultima letra 'a' esta na posicao {}""".format(frase.count("a"),frase.find("a")+1,frase.rfind("a")+1))

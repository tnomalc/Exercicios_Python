'''
 Escreva um programa que leia uma string e, em seguida, imprima a string lida removendo todos os espaços.
'''

#!/usr/bin/env python

minhaString = input("Por obséquio, digite a cadeia de caracteres desejada: \n")

texto = minhaString.split()

print("".join(texto))


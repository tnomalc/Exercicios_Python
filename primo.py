'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

#!/usr/bin/env python

num = int(input("Por favor, digite um número inteiro: \n"))

if num == 1:
  print("Não é primo")

elif num>2 and num%2 == 0 :
  print("Não é primo")
  
elif num%1 == 0 and num%num == 0:
  print("É primo")

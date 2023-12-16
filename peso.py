"""
  Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
 Para homens: (72.7*h) - 58
 Para mulheres: (62.1*h) - 44.7 
"""

#!/usr/bin/env python

H = float(input("Por favor, digite a sua altura: \n"))
genero = input("Digite o gênero('M' ou 'F'): \n")

if genero == 'F' :
  peso = 62.1*H - 44.7
  print(peso)
else:
  peso = 72.7*H - 58
  print(peso)



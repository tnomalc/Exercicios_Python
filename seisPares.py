"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

#!/usr/bin/env python

t,soma=1,0

for t in range(6):
   num = int(input("Por obséquio, digite um número inteiro: \n\a"))
   if num%2 == 0:
     soma+=num
     
print("A soma dos números pares inseridos é %d\n"%soma)

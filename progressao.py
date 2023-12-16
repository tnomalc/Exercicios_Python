"""
Desenvolva um programa que leia o primeiro termo e a razão e uma PA. No final,mostre os 10 primeiros termos dessa progressão.
"""

#!/usr/bin/env python

a1 = int(input("Por favor, digite o primeiro termo da progressão: \n"))
razao = int(input("Agora, digite a razão da progressão: \n"))

a10 = a1 + 9*razao
r = razao
print(a1)
for r in range(razao,a10,+razao):
  print(a1+r)


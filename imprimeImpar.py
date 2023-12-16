'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
de três e que se encontram no intervalo de 1 até 500.
'''

#!/usr/bin/env python

for r in range(1,500,+1):
   if r%2 != 0 and r%3 == 0:
      print(r)


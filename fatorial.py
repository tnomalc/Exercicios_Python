#!/usr/bin/env python

n = int(input("Digite um número inteiro positivo: \n"))
fatorial = 1
for i in range(1,n+1):
  fatorial*=i
print(fatorial)

#!/usr/bin/env python 

def calcula(x):
  f = (x**2 -3*x + 2)/x**3+2*x
  return f

x = int(input("Digite o valor da variável x"))

print(calcula(x))

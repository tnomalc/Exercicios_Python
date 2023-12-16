#!/usr/bin/env python

def retornaPalavra(a):
  texto = a.split()
  return texto[0]
  
a = input("Digite uma frase: \n")
print(retornaPalavra(a))


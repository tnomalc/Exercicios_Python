#!/usr/bin/env python

def invertePalavra(frase):
  reversa = frase[::-1]
  return reversa
  
frase = input("Digite uma frase: \n")
print(invertePalavra(frase))

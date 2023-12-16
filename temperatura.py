#!/usr/bin/env python

letra = input("Por obséquio, digite a sua opção 'C' ou 'F'")
valorTemperatura = float(input("Agora, insira o valor da temperatura: "))
if letra == 'C' :
  fahr = 1.8*valorTemperatura + 32
  print(fahr)
else :
  if letra == 'F':
    cel = 5.0/9(valorTemperatura - 32)
    print(cel)
  

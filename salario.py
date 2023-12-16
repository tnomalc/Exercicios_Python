#!/usr/bin/env python

SB = float(input("Por favor, digite o valor do salário bruto: "))

if SB>=500 or SB<800:
   SL = SB * 0.90
   print("O salário líquido é",SL)
elif SB>800 or SB<1000 :
   SL = SB * 0.85
   print("O salário líquido é",SL)
elif SB>=100 :
    SL = SB * 0.2
    print("O salário líquido é",SL)
else :
    print("O salário líquido é",SL)
 

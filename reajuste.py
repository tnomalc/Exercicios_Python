'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu
aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os
inferiores o iguais, o aumento é de 15%.
'''
#!/usr/bin/env python 

salarioVigente = float(input("Digite o salário: \n\a"))

if salarioVigente > 1250 :
   salarioReajustado = salarioVigente * 1.10
   print("O salário corrigido é %.5f\n"%salarioReajustado)

else :
   salarioReajustado = salarioVigente * 1.15
   print("O salário corrigido é %.5f\n\a"%salarioReajustado)
   


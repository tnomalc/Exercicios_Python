"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com
15% de aumento.
"""
#!/usr/bin/env python

salAtual = float(input("Insira o valor do salário vigente: \n\a"))

# Fator de aumento: (100/100) + (15/100) = 1 + 0.15 = 1,15
salReajustado = salAtual * 1.15

print("O salário com aumento é de %.4f\n"%salReajustado)

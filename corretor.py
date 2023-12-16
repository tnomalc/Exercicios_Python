#!/usr/bin/env python 

nome = input("Por favor, digite o nome da corretora(or): \n")
quantImoveisVendidos = int(input("Informe a quantidade de imóveis comercializados: \n"))
totalVendas = float(input("Digite o valor total das vendas: \n"))

salTotal = 1500 + quantImoveisVendidos*200 + totalVendas*(5/100)

print("%s terá o salário de %f\n"%(nome,salTotal))

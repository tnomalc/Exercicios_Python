'''
 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de
desconto.
'''
#!/usr/bin/env python

precoProduto = float(input("Digite o valor do produto: \n"))

# Fator de diminuição: (100/100) - (5/100) = 1 - 0,05 = 0,95
precoNovo = precoProduto * 0.95

print("O preço do produto com desconto é de %.6f\n"%precoNovo)

#!/usr/bin/env python 

num1 = int(input("Por obséquio, digite o primeiro número: "))
num2 = int(input("Por obséquio, digite o segundo número: "))
operador = input("Digite o operador aritmético '+','-','*' ou '/'")


if operador == '+' : 
  print("A soma dos números é ",num1+num2)
elif operador == '-' : 
  print("A diferença dos números é ",num1-num2)
elif operador == '*' : 
  print("O produto entre os números é",num1*num2)
else :
  print("O resultado é ",num1/num2)



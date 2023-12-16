#!/usr/bin/env python 

num1 = int(input("Digite um valor inteiro: \n"))
num2 = int(input("Digite outro valor: \n"))

antigoNum1 = num1
antigoNum2 = num2

trocaVar = num1
num1 = num2
num2 = trocaVar

print("O número ",antigoNum1,"agora é",num1,sep=" ")
print("O número ",antigoNum2,"agora é",num2,sep=" ")



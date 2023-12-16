#!/usr/bin/env python

nome = input("Digite o nome: \n")
sexo = input("Digite \"Masculino\" ou \"Feminino\"")
idade = int(input("Digite a idade: \n")

if sexo == "Feminino" and idade <= 25 :
  print("ACEITA")

else :
  print("NÃO ACEITA")

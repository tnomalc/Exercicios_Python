#!/usr/bin/env python

import math

x1 = float(input("Digite o valor da abscissa do primeiro ponto: \n"))
y1 = float(input("Digite o valor da ordenada do primeiro ponto: \n"))

x2 = float(input("Digite o valor da abscissa do segundo ponto: \n"))
y2 = float(input("Digite o valor da ordenada do segundo ponto: \n"))

d = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))

print("O valor procurado é %.5f\n"%d)

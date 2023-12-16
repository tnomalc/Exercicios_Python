#!/usr/bin/env python
import math

num = int(input("Digite um número inteiro positivo: \n"))

if num%2 == 0 :
     print(math.pow(num,2))
else :
    print(math.pow(num,3))

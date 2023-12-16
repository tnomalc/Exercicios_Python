#!/usr/bin/env python
import math

b = -4.7
a = 1.41
c = -5.58

delta = math.pow(b,2) - 4*a*c
print("O determinante da equação quadrática é %.5f"%delta)

if delta > 0 :
 x1 = (-b+math.sqrt(delta))/2*a
 x2 = (-b-math.sqrt(delta))/2*a
 print(x1,x2)

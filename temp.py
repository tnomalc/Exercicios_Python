'''
 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
 Autor: Rainério Calmont Junior
 Powered: FreeBSD 14, Emacs, and GCC.
 Data: 07 de dezembro de 2023
'''
#!/usr/bin/env python

fahr = float(input("Por obséquio, digite o valor da temperatura em Fahrenheit: \n"))

cel = 5/9.0*(fahr-32)

print("A temperatura ",fahr,"em graus Fahrenheit","é ",cel,"em graus Celsisus",sep=" ")

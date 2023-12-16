'''
 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''
#!/usr/bin/env python

cel = float(input("Insira o valor da temperatura em graus celsius: \n\a"))

fahr = 1.8*cel + 32

print("A temperatura ",cel,"em graus Celsius","é igual a ",fahr,"na escala Fahrenheit.",sep=" ")

# Questão 3
import math

def potencia(a, b):
   resultado = math.pow(a, b)
   print(resultado)

d1, d2 = input().split()
d1 = float(d1)
d2 = float(d2)

potencia(d1, d2)
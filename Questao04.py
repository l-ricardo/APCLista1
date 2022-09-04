# Questão 4
import math

def potencia(a, b):
   resultado = math.pow(a, b)
   print(resultado)

def powAPC():
   d1, d2 = input().split()
   d1 = int(d1)
   d2 = int(d2)
   potencia(d1, d2)
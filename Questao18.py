 # Questão 18
def concatenar(str1, str2):
    resultado1 = str1 + str2
    print(resultado1)

def repetir(a, str1):
    resultado2 = int(a) * str1
    print(resultado2)

def ambos(str1, str2, a):
    resultado3 = int(a) * (str1 + str2)
    print(resultado3)

str1, str2, a = input().split()

concatenar(str1, str2)
repetir(a, str1)
ambos(str1, str2, a)
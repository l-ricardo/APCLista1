# Questão 10
def conta(idade):
    A = idade/360
    M = (idade%360)/30
    D =(idade%360)%30
    print(str(int(A)) + ' ' + str(int(M)) + ' ' + str(int(D)))

def age(a,b,c):
    conta(a)
    conta(b)
    conta(c)
    
d1, d2, d3 = input().split()
d1 = int(d1)
d2 = int(d2)
d3 = int(d3)
age(d1, d2, d3)
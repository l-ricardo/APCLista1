# Questão 14
def quantosSemestres(m, a, s):
    a_m = int(str(m)[:2]) + 2000
    print(2 * (a - a_m) - int(str(m)[3]) + s)
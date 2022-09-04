# Questão 15
def qualPeriodo(m, a, s):
    a_m = int(str(m)[:2]) + 2000
    s_m = int(str(m)[3])
    print((((a - a_m) * 2))- s_m + s + 1)
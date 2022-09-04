# Questão 11
def peso_ideal(alt):
    ideal_H = 72.7 * alt - 58
    ideal_M = 62.1 * alt - 44.7
    print(format(ideal_H, ".2f"), format(ideal_M, ".2f"))

altura = float(input())
peso_ideal(altura)
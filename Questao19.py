# Questão 19
def pacotesDeBolacha(m, n, k):
    if (n * k) <= m:
        print(m - (n * k))
    else:
        print(m - int(m/n) * n)
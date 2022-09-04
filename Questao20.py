# Questão 20
def pacotesDeBolacha(m, n, k):
    print(m - (n * k))
    if (n * k) <= m:
        print(m - (n * k))
    else:
        print(m - int(m/n) * n)
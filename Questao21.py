# Questão 21
def print_rectangle(x):
    print(x)
    print('+' * x)
    print('+' + ' ' * (x - 2) + '+')
    print('+' * x)

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print_rectangle(a)
print_rectangle(b)
print_rectangle(c)
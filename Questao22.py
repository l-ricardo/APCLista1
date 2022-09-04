# Questão 22
def print_rectangle(x):
    print(x)
    print('x' * x)
    print('x' + ' ' * (x - 2) + 'x')
    print('x' + ' ' * (x - 2) + 'x')
    print('x' * x)

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print_rectangle(a)
print_rectangle(b)
print_rectangle(c)
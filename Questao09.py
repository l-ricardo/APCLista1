# Questão 9
def age(a, b, c):
    print(str(int(a/360)) + ' ano(s), ' + str(int((a%360)/30)) + ' mes(es) e ' + str(int((a%360)%30)) + ' dia(s)')
    print(str(int(b/360)) + ' ano(s), ' + str(int((b%360)/30)) + ' mes(es) e ' + str(int((b%360)%30)) + ' dia(s)')
    print(str(int(c/360)) + ' ano(s), ' + str(int((c%360)/30)) + ' mes(es) e ' + str(int((c%360)%30)) + ' dia(s)')
    
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
age(a, b, c) 
# Questão 31
tempo = input()
h = int(tempo[0:2])
min = int(tempo[3:5])
seg = int(tempo[6:8])
x = seg + min * 60 + h * 3600

print('La se foram ' + str(x) + ' segundos que nao voltam mais...')
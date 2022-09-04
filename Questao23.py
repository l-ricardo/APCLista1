# Questão 23
def ritmoMedio(h,  m,  s,  d):
    s += h  *  3600 + m  *  60
    mediaMinutos = str(int(s/60//d))
    mediaSegundos = str(int(s/60%d/d*60))
    print(f'{mediaMinutos.zfill(2)}:{mediaSegundos.zfill(2)} min/km')
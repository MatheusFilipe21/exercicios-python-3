m = float(input('Escreva uma distâcia em metros: '))
print('Sua distância em kilômetros é:\033[36m{:.1f}\033[m'.format(m*0.001))
print('Sua distância em hectômetros é:\033[35m{:.1f}\033[m'.format(m*0.01))
print('Sua distância em decâmetros é:\033[34m{:.1f}\033[m'.format(m*0.1))
print('Sua distância em decímetros é:\033[33m{:.1f}\033[m'.format(m*10))
print('Sua distância em centímetros é:\033[32m{:.1f}\033[m'.format(m*100))
print('Sua distância em milímetros é:\033[31m{:.1f}\033[m'.format(m*1000))

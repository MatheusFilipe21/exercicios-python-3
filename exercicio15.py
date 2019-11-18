d = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos quilômetros foram percorridos pelo carro: '))
p = (d * 60) + (km * 0.15)
print('O valor pelo aluguel do carro é:\033[33m{:.2f}\033[m'.format(p))

d = int(input('Digite a distância da sua viagem em KM: '))
if d > 200:
    print('O valor da sua viagem será de R$ \033[1;32m{:.2f}\033[m'.format(d * 0.45))
elif d < 0:
    print('\033[4;31mNão é possível fazer uma viagem com esse valor!\033[m')
else:
    print('O valor da sua viagem será de R$ \033[36m{:.2f}\033[m'.format(d * 0.5))

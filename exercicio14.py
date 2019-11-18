temp = float(input('Escreva a temperatura em °C: '))
novatemp = (temp * 1.8) + 32
print('A temperatura de \033[34m{:.2f}\033[m em °C equivale a \033[31m{:.1f}\033[m°F'.format(temp, novatemp))

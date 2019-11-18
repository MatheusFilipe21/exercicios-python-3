l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros : '))
t = (l*a)/2
print('Uma parede de largura \033[34m{:.2f}m\033[m e altura \033[31m{:.2f}m\033[m necessita de \033[32m{:.2f}\033[m litros de tinta para ser pintada' .format(l, a, t))

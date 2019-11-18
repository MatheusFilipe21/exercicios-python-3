import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print('O comprimento da Hipotenusa desse triângulo é \033[35m{:.2f}\033[m'.format(h))

import math
a = float(input('Digite o valor de um ângulo: '))
print('O seno do ângulo é:\033[32m{:.2f}\033[m'.format(math.sin(math.radians(a))))
print('O cosseno do ângulo é:\033[31m{:.2f}\033[m'.format(math.cos(math.radians(a))))
print('A tangente do ângulo é:\033[34m{:.2f}\033[m'.format(math.tan(math.radians(a))))

numero = int(input('Digite um número de 0 até 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número \033[31m{}\033[m'.format(numero))
print('Unidade:\033[32m{}\033[m'.format(u))
print('Dezena:\033[33m{}\033[m'.format(d))
print('Centena:\033[34m{}\033[m'.format(c))
print('Milhar:\033[35m{}\033[m'.format(m))

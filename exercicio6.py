n = float(input(' Escreva um número: '))
print('O dobro desse número é: \033[31m{}\033[m'.format(n*2))
print('O triplo desse número é: \033[32m{}\033[m'.format(n*3))
print('A raiz quadrada desse número é: \033[33m{:.2f}\033[m'.format(n**(1/2)))

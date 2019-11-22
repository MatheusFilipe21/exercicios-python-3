a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
if a > b:
    print('\033[31m{:.2f}\033[m é maior que \033[34m{:.2f}\033[m!'.format(a, b))
elif a < b:
    print('\033[34m{:.2f}\033[m é maior que \033[31m{:.2f}\033[m!'.format(b, a))
else:
    print('Não existe valor maior, \033[36m{:.2f}\033[m é igual a \033[36m{:.2f}\033[m!'.format(a, b))

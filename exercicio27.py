nome = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é \033[35m{}\033[m'.format(nome[0]))
print('Seu último nome é \033[36m{}\033[m'.format(nome[len(nome) - 1]))

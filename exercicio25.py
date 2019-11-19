nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? \033[1;32m{}\033[m'.format('SILVA' in nome.upper()))

n = int(input('Escreva um número: '))
print('O antecessor do seu número é: \033[1;31;40m{}\033[m'.format(n-1))
print('O sucessor do seu número é: \033[1;30;41m{}\033[m'.format(n+1))

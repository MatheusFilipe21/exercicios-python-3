n = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão: \n\033[31m[1] Binário\033[m \n\033[34m[2] Octal\033[m \n\033[35m[3] Hexadecimal\033[m')
opcao = int(input('Digite uma opção: '))
if opcao == 1:
    print('{} convertido para Binário é igual a \033[31m{}\033[m'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a \033[34m{}\033[m'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a \033[35m{}\033[m'.format(n, hex(n)[2:]))
else:
    print('\033[1;30;41mVocê digitou uma opção inválida!')
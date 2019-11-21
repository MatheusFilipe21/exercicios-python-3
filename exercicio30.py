n = int(input('Digite um número inteiro: '))
n = n % 2
if n == 0:
    print('O número digitado é \033[34mPar\033[m!!')
else:
    print('O número digitado é \033[36mÍmpar\033[m!!')

n = c = soma =0
n = int(input('Digite números inteiros ou ditite 999 para sair: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite números inteiros ou ditite 999 para sair: '))
print('Foram digitados {} números e a soma entre eles é {}.'.format(c, soma))
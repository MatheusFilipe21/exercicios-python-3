n = soma = c = maior = menor = 0
cont = 'S'
while cont in 'Ss' :
    n = int(input('Digite números inteiros: '))
    c += 1
    soma += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    cont = str(input('Deseja continuar (S/N): ')).upper().strip()[0]
media = soma / c
print('A media entre os valores digitados é {} o maior é {} e o menor é {}.'.format(media, maior, menor))
import random
cont = 0
acertou = False
computador = random.randrange(11)
while not acertou:
    numero = int(input('Digite um número de (0 a 10): '))
    if 0 <= numero <= 10:
        cont += 1
        if numero == computador:
            acertou = True
        else:
            if numero > computador:
                print('Menos... tente novamente: ')
            else:
                print('Mais... tente novamente: ')
    else:
        acertou = False
print('Parabéns você venceu o computador, foram necessárias {} chances.'.format(cont))
from random import randint
from time import sleep
lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Digite a sua opção: '))
if 0 < jogada > 2:
    print('OPÇÃO INVÁLIDA')
else:
    print('-=-' * 12)
    print('Você jogou {}'.format(lista[jogada]))
    sleep(1)
    print('O computador jogou {}'.format(lista[computador]))
    print('-=-' * 12)
    print('')
    if computador == 0:
        if jogada == 0:
            print('EMPATE')
        elif jogada == 1:
            print('O JOGADOR VENCEU')
        elif jogada == 2:
            print('O COMPUTADOR VENCEU')
    elif computador == 1:
        if jogada == 0:
            print('O COMPUTADOR VENCEU')
        elif jogada == 1:
            print('EMPATE')
        elif jogada == 2:
            print('O JOGADOR VENCEU')
    else:
        if jogada == 0:
            print('O JOGADOR VENCEU')
        elif jogada == 1:
            print('O COMPUTADOR VENCEU')
        elif jogada == 2:
            print('EMPATE')

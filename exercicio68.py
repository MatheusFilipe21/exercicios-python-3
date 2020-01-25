from random import randint
cont = 0
while True:
    n = int(input('Digite um número: '))
    ncomputador = randint(0, 10)
    total = n + ncomputador
    op = ' '
    while op not in 'PI':
        op = str(input('Escolha Par ou Ímpar (P/I): ')).strip().upper()[0]
    print(f'Você jogou {n} o computador jogou {ncomputador} o total deu {total}')
    if op == 'P':
        if total % 2 == 0:
            print('O jogador Venceu!')
            cont += 1
        else:
            print('O computador Venceu!')
            break
    elif op == 'I':
        if total % 2 == 1:
            print('O jogador Venceu!')
            cont += 1
        else:
            print('O computador Venceu!')
            break
    print('Vamos de novo...')
print(f'O jogador ganhou {cont} vezes.')

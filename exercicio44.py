p = float(input('Digite o valor do produto: '))
print('-' * 20)
print('''Escolha a forma de pagamento:
[1] Dinheiro ou cheque ou no débito
[2] Em 1x no cartão de crédito
[3] Em 2x no cartão de crédito
[4] Em 3x no cartão de crédito''')
print('-' * 20)
fp = int(input('Digite a forma de pagamento escolhida: '))
if fp == 1:
    print('Você pagaria R$\033[33m{}\033[m, mas como você pagará à vista só irá pagar R$\033[36m{:.2f}\033[m'.format(p, (p * 0.9)))
elif fp == 2:
    print('Você pagaria R$\033[33m{}\033[m, mas nessa opção você pagará em 1x no cartão de crédito R$\033[36m{:.2f}\033[m'.format(p, (p * 0.95)))
elif fp == 3:
    print('Você pagará R$\033[33m{}\033[m em 2x no cartão de crédito de RS\033[36m{:.2f}\033[m sem juros!'.format(p, p/2))
elif fp == 4:
    print('Você pagaria R$\033[33m{}\033[m, mas nessa opção você pagará em 3x no cartão de crédito de R$\033[36m{}\033[m'.format(p, (p * 1.2 / 3)))
else:
    print('\033[1:31mForma de pagamento inválida!\033[m')

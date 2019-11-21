s = float(input('Digite o valor do seu salário: '))
if s <= 1250:
    print('O seu salário que era de R$ \033[36m{}\033[m será reajustado para R$ \033[4;32m{:.2f}\033[m'.format(s, (s*(1.15))))
else:
    print('O seu salário que era de R$ \033[36m{}\033[m será reajustado para R$ \033[4;34m{:.2f}\033[m'.format(s, s * (1.1)))

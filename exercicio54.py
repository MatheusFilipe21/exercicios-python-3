from datetime import date
ma = 0
me = 0
for c in range(1, 8):
    a = int(input('Digite o ano da pessoa {}: '.format(c)))
    ano = date.today().year - a
    if ano >= 21:
        ma += 1
    else:
        me += 1
print('Dentre as sete pessoas \033[32m{}\033[m são maiores de idade e \033[36m{}\033[m são menores de idade!'.format(ma, me))

ano = int(input('Digite o valor do ano que você deseja saber se ele é bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} \033[36mé\033[m um ano bissexto!!'.format(ano))
else:
    print('O ano de {} \033[31mnão é\033[m um ano bissexto!'.format(ano))

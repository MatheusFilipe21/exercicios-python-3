velo = int(input('Digite a sua velocidade em KM/H: '))
if (velo < 0):
    print('\033[31mNão é possível ter uma velocidade com esse valor!!\033[m')
elif (velo > 0) and (velo <= 80):
    print('\033[33mVocê está dirigindo em uma velocidade ótima!!\033[m')
elif (velo == 0):
    print('\033[4;32mVocê já pode dar saída com o carro!!\033[m')
else:
    print(' Você terá que pagar uma multa no valor de R$ \033[1;31m{}\033[m , dirija com mais prudência!!'.format((velo-80) * 7))

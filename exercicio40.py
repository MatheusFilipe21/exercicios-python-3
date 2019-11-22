n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if (media >= 7):
    print('Parabéns você foi \033[36mAPROVADO\033[m, sua média foi {:.2f}'.format(media))
elif (media >= 4) and (media <= 6.9):
    print('Sua média foi {:.2f}, você terá que fazer uma prova de \033[33mRECUPERAÇÃO\033[m!'.format(media))
    print('Na \033[33mRECUPERAÇÃO\033[m você precisa tirar {:.2f}para ser aprovado!'.format(10 - media))
else:
    print('Você foi \033[31mREPROVADO\033[m!')

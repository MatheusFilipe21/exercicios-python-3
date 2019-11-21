import random
numero = int(input('Digite um número de (0 a 5): '))
if numero == random.randrange(6):
    print('\033[30;42mParabéns você venceu do computador!!\033[m')
elif (numero < 0) or (numero > 5):
        print('\033[4;30;41mVocê digitou um valor inválido!\033[m')
else:
        print('\033[7;33;40mInfelizmente o computador lhe venceu!\033[m')

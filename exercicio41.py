from datetime import date
a = int(input('Digite o seu ano de nascimento: '))
idade = (date.today().year - a)
if idade < 0:
    print('\033[31mNão é possível você ter nascido nesse ano\033[m ou\033[33m a data do seu computador está '
          'incorreta\033[m!')
elif (idade >= 0) and (idade <= 9):
    print('Você está na categoria \033[32mMIRIM\033[m')
elif (idade > 9) and (idade <= 14):
    print('Você está na categoria \033[34mINFANTIL\033[m')
elif (idade > 14) and (idade <= 19):
    print('Você está na categoria \033[35mJUNIOR\033[m')
elif (idade > 19) and (idade <= 25):
    print('Você está na categoria \033[36mSÊNIOR\033[m')
else:
    print('Você está na categoria \033[7;37mMASTER\033[m')
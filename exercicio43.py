a = float(input('Digite sua altura em metros: '))
p = float(input('Digite seu peso em Kg: '))
imc = p / (a**2)
print('Seu IMC é {:.1f} e você está na categoria '.format(imc), end='')
if imc < 18.5:
    print('\033[31mABAIXO DO PESO\033[m')
elif 18.5 <= imc <= 24.9:
    print('\033[32mPESO IDEAL\033[m')
elif 25 <= imc <= 29.9:
    print('\033[34mSOBREPESO\033[m')
elif 30 <= imc <= 34.9:
    print('\033[35mOBESIDADE GRAU 1\033[m')
elif 35 <= imc <= 39.9:
    print('\033[33mOBESIDADE GRAU 2\033[m')
else:
    print('\033[31mOBESIDADE GRAU 3\033[m')

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece \033[31m{}\033[m vezes.'.format(frase.count('A')))
print(('A primeira letra A aparece na posição \033[36m{}\033[m'.format(frase.find('A') + 1)))
print('A última letra A aparece na posição \033[34m{}\033[m'.format(frase.rfind('A') + 1))

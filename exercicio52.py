n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m',end='')
    print('{} '.format(c), end='')
print('\n\033[36mO número foi dividido {} vezes\033[m'.format(t))
if t == 2:
    print('\033[34mO número digitado é PRIMO!\033[m')
else:
    print('\033[34mO número digitado não é PRIMO!\033[m')

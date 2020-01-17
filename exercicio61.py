n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c <= 10:
    print('{} '.format(n), end='')
    n += r
    c += 1

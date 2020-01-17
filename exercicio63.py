n = int(input('Digite a quantidade de termos que você deseja saber da sequência de Fibonnaci: '))
n1 = 0
n2 = 1
c = 0
while c != n:
    if c % 2 == 0:
        print('{} -> '.format(n1), end='')
        c += 1
        n1 += n2
    else: 
        print('{} -> '.format(n2), end='')
        c += 1
        n2 += n1
print('FIM')
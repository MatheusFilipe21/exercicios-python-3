n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
tot = 0
mais = 10
while mais != 0:    
    tot += mais
    while c <= tot:
        print('{} '.format(n), end='')
        n += r
        c += 1
    mais = int(input('\nMais quantos termos você deseja saber: '))
print('O total de termos mostrados foram {}.'.format(tot))
s = 0
count = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor:'.format(c)))
    if n % 2 == 0:
        s += n
        count += 1
print('Você informou {} números pares e a soma de todos os números pares vale {}'.format(count, s))
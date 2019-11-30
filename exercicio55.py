maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Digite o peso da {} pessoa: '.format(c)))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso é {:.2f} e o menor peso é {:.2f}'.format(maior, menor))

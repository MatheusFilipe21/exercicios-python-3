tot = contmil = menor = cont = 0
maisbarato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto R$: '))
    cont += 1
    tot += preco
    if preco > 1000:
        contmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        maisbarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R$: {tot:.2f}.')
print(f'{contmil} produtos custam mais do que R$1000.')
print(f'O produto mais barato foi {maisbarato} custando R${menor:.2f}.')

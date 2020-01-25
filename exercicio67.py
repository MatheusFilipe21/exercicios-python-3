while True:
    n = int(input('A tabuada de qual número você quer saber: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} é {n * c}')
print('Programa Finalizado!')

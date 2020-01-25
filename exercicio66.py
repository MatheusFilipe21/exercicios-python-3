n = c = soma =0
while True:
    n = int(input('Digite números inteiros ou ditite 999 para sair: '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Foram digitados {c} números e a soma entre eles é {soma}.')
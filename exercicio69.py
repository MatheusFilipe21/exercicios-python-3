cont18 = conth = contm20 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa (M/F)')).strip().upper()[0]
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar (S/N): ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {cont18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {conth} homens.')
print(f'Foram cadastradas {contm20} mulheres com menos de 20 anos.')

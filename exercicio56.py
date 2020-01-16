somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('----- {} Pessoa -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (m/f): ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média da idade do grupo é {:.2f}'.format(mediaidade))
print('O nome do homem mais velho é {} e a sua idade é {} anos!'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

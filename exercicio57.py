sexo = str(input('Digite seu sexo (M/F): ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Dados incorretos. Digite seu sexo: ')).upper()[0].strip()
print('Sexo {} registrado com sucesso!'.format(sexo))
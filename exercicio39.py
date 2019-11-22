from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
anoa = date.today().year
idade = anoa - ano
anop = anoa + (18 - (anoa - ano))
if idade < 18:
    print('Você tem \033[33m{}\033[m anos e a idade para o alistamento é 18 anos, o ano em que você deve se alistar é \033[36m{}\033[m!'.format(idade, anop))
elif idade == 18:
    print('Você tem \033[33m{}\033[m anos, faça seu alistamento \033[32mIMEDIATAMENTE\033[m!'.format(idade, anoa))
else:
    print('Seu ano de alistamento já passou, o ano do seu alistamento foi \033[31m{}\033[m!'.format(anop))

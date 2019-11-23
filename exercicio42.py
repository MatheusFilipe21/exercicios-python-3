r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('\033[32mOs segmentos acima podem formar um triângulo.\033[m')
    if r1 == r2 and r1 == r3:
        print('O triângulo formado será um \033[1;34mEquilátero\033[m, que possui todos os seus segmentos iguais!')
    elif r1 == r2 or r1 == r3:
        print('O triângulo formado será um \033[1;35mIsóceles\033[m, que possui dois dos seus segmentos iguais!')
    else:
        print('O triângulo formado será um \033[1;36mEscaleno\033[m, que possui todos os seus segmentos diferentes!')
else:
    print('\033[31mOs segmentos acima não podem formar um triângulo.\033[m')

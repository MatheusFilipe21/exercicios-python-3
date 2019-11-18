import random
a1 = str(input('Digite o nome de um aluno: '))
a2 = str(input('Digite o nome de outro aluno: '))
a3 = str(input('Digite o nome de mais um aluno: '))
a4 = str(input('Digite o nome do último aluno: '))
alunos = [a1, a2, a3, a4]
print('O aluno que vai apagar o quadro é \033[1;32m{}\033[m'.format(random.choice(alunos)))

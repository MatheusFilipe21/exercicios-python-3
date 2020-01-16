n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar 
    [3] Maior 
    [4] Novos números 
    [5] Sair do programa''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto entre {} e {} vale {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
        elif n1 == n2: 
            print('Não existe número maior')
        else:
            maior = n2
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente')
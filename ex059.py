from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print(''' ------MENU------
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa''')
    opção = int(input('Qual a sua opção?: '))
    print('-='*10)
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} e {} é: {}'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('A Multiplicação de {} e {} é: {}'.format(n1, n2, mult))
    elif opção == 3:
        maior = 0
        if n1 > n2:
            maior = n1
            print('O maior é: {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior é: {}'.format(maior))
        elif n1 == n2:
            print('Os dois são iguais!')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('FINALIZANDO...')
    else:
        print('Opção inválida, tente novamente')
print('volte sempre!!')


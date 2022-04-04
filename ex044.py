#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format("LOJAS CARVALHO"))
produto = float(input('Valor do Produto R$: '))
print(''' FORMA DE PAGAMENTO:
[ 1 ] A VISTA: DINHEIRO OU CHEQUE
[ 2 ] A VISTA: CARTÃO DE DÉBITO
[ 3 ] ATÉ 2X NO CARTÃO DE CRÉDITO.
[ 4 ] PARCELADO NO CARTÃO DE CREDITO (3X OU +)''')
opção = int(input('Qual a forma de pagamento?: '))
if opção == 1:
    print('A VISTA: DINHEIRO OU CHEQUE. PARA ESTA OPÇÃO 10% DE DESCONTO')
    total = produto - (produto * 10 / 100)
    print(f'Valor total da compra: R${total:.2f}')
elif opção == 2:
    print('A VISTA: CARTÃO DE DÉBITO. PARA ESTA OPÇÃO 5% DE DESCONTO.')
    total = produto - (produto * 5 / 100)
    print(f'Valor total de compra: R${total:.2f}')
elif opção == 3:
    print('Em até 2x no Cartão de Crédito.')
    qtdparcelas = int(input('1x ou 2x?'))
    if qtdparcelas == 1:
        total = produto
        print(f'O valor de R${total:.2f} será cobrado integral na proxima fatura.')
    elif qtdparcelas == 2:
        total = produto / 2
        print(f'O valor de R${produto:.2f} será cobrado em 2x SEM JUROS de {total:.2f}')
elif opção == 4:
    qtdparcelas = int(input('Em quantas vezes deseja parcelar? (min 3 max 10)'))
    total = produto + (produto * 20 / 100)
    totparcelado = total / qtdparcelas
    print(f'O valor de R${produto:.2f} será parcelado em {qtdparcelas} vezes COM JUROS de R${totparcelado:.2f}')
    print(f'Valor total da compra R${total:.2f}')
else:
    print('Opção inválida.')








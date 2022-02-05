compras = float(input('Preço das compras:R$'))
print('''FORMAS DE PAGAMENTO
[  1  ]A vista Dinheiro ou Cheque
[  2  ]A vista no Cartão
[  3  ]Até 2x no Cartão
[  4  ]3x ou mais no Cartão''')
opção = int(input('Sua opção: '))
if opção == 1:
    total = compras - (compras * 10 / 100)
elif opção == 2:
    total = compras - (compras * 5 / 100)
elif opção == 3:
    total = compras
    parcela = compras / 2
    print('R${:.2f} EM 2X SEM JUROS SERÁ R${:.2f}'.format(compras, parcela))
elif opção == 4:
    qtdparcelas = int(input('Quantidade de parcelas: '))
    total = compras + (compras * 20 / 100)
    parcelas = total / qtdparcelas
    print('R${:.2f} em {}x COM JUROS SERÁ R${:.2f}'.format(compras, qtdparcelas, parcelas))
else:
    total = compras
    print('Opção inválida, tente novamente!')
print('Sua compra de R${:.2f} custara no final R${:.2f}'.format(compras, total))

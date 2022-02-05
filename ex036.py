casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o sálario do comprador: R$'))
anos = int(input('Digite o número de anos que deseja simular o financiamento: '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para comprar uma casa no valor de {:.2f} ganhando {:.2f} o valor da prestação será de: R${:.2f}'.format(casa, salario, prestação))
if prestação > minimo:
    print('Emprestimo negado, o valor da prestação supera 30% do seu sálario!')
else:
    print('Emprestimo concedido!!')





d = float(input('Digite a quantidade de dias de aluguel: '))
km = float(input('Digite a quantidade de km rodados: '))
aluguel = (d * 60) + (0.15 * km)
print('O total a pagar é de R${:.2f}'.format(aluguel))



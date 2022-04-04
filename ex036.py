#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o salário do comprador: '))
anos = int(input('Em quantos anos deseja simular?: '))
prestacao = casa / (anos * 12)
minimo = (salario * 30 / 100)
print(f'Para financiar uma casa no valor de R${casa:.2f}')
print(f'A parcela será de R${prestacao:.2f}')
if prestacao < minimo:
    print('Emprestimo Aprovado!!')
else:
    print('Emprestimo Negado.')

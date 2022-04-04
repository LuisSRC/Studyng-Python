#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('-' * 50)
print('{:^40}'.format("LISTAGEM DE PREÇOS"))
print('-' * 50)
materiais = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
             'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso',
             9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro',
             34.90)
for pos in range(0, len(materiais)):
    if pos % 2 == 0:
        print('{:.<40}'.format(materiais[pos]), end='')
    else:
        print('R$ {:>.2f}'.format(materiais[pos]))
print('-' * 50)
































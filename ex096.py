#Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def área(l, c):
    a = l * c
    print(f'A área de um terreno de {l}x{c} é {a}m²')


print('Controle de Terrenos')
print('-' * 30)
largura = float(input('LARGURA: '))
compr = float(input('COMPRIMENTO: '))
área(largura, compr)




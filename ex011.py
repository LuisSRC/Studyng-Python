#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
print(f'Sua parede tem {largura} de largura e {altura} de altura. Area total de {area}')
tinta = area / 2
print(f'Você precisará de {tinta}l de tinta')


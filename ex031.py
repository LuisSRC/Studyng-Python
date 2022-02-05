distancia = float(input('Digite a distância da viagem em km: '))
if distancia <= 200:
    preco = 0.5 * distancia
    print('O valor da passagem para a viagem de {:.2f}km será de R${:.2f}'.format(distancia, preco))
else:
    preco = 0.45 * distancia
    print('O valor da passagem para a viagem de {:.2f}km será de R${:.2f}'.format(distancia, preco))


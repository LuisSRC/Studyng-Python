velocidade = float(input('Digite qual é a velocidade atual do carro: '))
if velocidade >80:
    print('MULTADO!! Você excedeu o limite de velocidade da via que é de 80km/h!!')
    multa = (velocidade - 80) * 7
    print('Você sera multado em R${:.2f}!'.format(multa))
print('Dirija com cuidado, tenha um otimo dia!')

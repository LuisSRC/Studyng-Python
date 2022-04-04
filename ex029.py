#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você foi multado! O valor a ser pago é de: R${multa:.2f}')
else:
    print('Respeite os limites de velocidade!')
print('Boa viagem!')

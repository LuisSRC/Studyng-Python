peso = float(input('Digite o seu peso? (kg)'))
altura = float(input('Digite a sua altura: (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
print('Você esta:', end='')
if imc <= 18.5:
    print('Abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print(' no Peso ideal.')
elif imc > 25 and imc <= 30:
    print('em Sobrepeso')
elif imc >30 and imc <= 40:
    print(' em Obesidade')
else:
    print('em Obesidade Morbida')




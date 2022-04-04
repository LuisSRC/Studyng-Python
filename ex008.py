#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor = float(input('Digite um valor em metros: '))
print(f'{valor}m em KM é: {valor / 1000:.3f}km')
print(f'{valor}m em HM é: {valor / 100:.2f}hm')
print(f'{valor}m em DAM é: {valor / 10:.2f}dam')
print(f'{valor}m em DM é: {valor * 10:.2f}dm')
print(f'{valor}m em CM é: {valor * 100:.2f}cm')
print(f'{valor}m em MM é: {valor * 1000:.2f}mm')


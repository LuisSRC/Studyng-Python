import math
#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.
angulo = float(input('Digite o ângulo que você deseja: '))
print(f'O angulo de {angulo} tem o SENO de {math.sin(math.radians(angulo)):.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {math.cos(math.radians(angulo)):.2f}')
print(f'O angulo de {angulo} tem a TANGENTE de {math.tan(math.radians(angulo)):.2f}')

from math import hypot
#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa.
ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
hipotenusa = hypot(ca, co)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}')


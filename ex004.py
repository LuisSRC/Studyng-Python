##Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.
frase = str(input('Digite algo: '))
print(f'O tipo primitivo desse valor é: {type(frase)}')
print(f'Só tem espaços?: {frase.isspace()}')
print(f'É númerico?: {frase.isnumeric()}')
print(f'É alfabético?: {frase.isalpha()}')
print(f'Esta em MAISCULAS?: {frase.isupper()}')
print(f'Está em minusculas?: {frase.islower()}')
print(f'Está capitalizada?: {frase.istitle()}')
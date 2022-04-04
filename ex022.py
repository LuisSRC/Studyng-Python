#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Nome com todas as letras MAIUSCULAS: {nome.upper()}')
print(f'Nome com todas as letras minusculas: {nome.lower()}')
nomecompleto = nome.split()
juntatudo = ''.join(nomecompleto)
print(f'Nome sem considerar espaços tem {len(juntatudo)} letras.')
print(f'O primeiro nome é: {nomecompleto[0]} e tem {len(nomecompleto[0])} letras')



#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = média = maior = menor = cont = 0
resp = ''
while resp in 'S':
    num = int(input('Digite um número: '))
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
média = soma / cont
print(f'A média da soma dos números digitados é: {média}')
print(f'O MAIOR número lido foi {maior} e o menor foi {menor}')





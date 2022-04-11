#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'A lista contêm {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem DECRESCENTE: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da Lista!')
else:
    print('O valor 5 não foi digitado.')


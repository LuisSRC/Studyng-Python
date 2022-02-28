soma = qtd = media = maior = menor = 0
resp = 'S'
while resp != 'N':
    n = int(input('Digite um número: '))
    qtd += 1
    soma += n
    media = soma / qtd
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if qtd == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média foi {:.2f}'.format(qtd, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))



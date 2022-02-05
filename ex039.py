from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Você ainda tem {} anos de idade!'.format(idade))
    saldo = 18 - idade
    print('Ainda faltam {} anos para se alistar!'.format(saldo))
    print('Você deverá se alistar em {} '.format(saldo + atual))
else:
    print('Você tem {} anos de idade!'.format(idade))
    saldo = idade - 18
    print('Seu alistamento foi a {} anos'.format(saldo))
    print('Você deveria ter se alistado em {}'.format(atual - saldo))


















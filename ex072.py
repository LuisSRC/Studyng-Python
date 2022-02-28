resp = ''
números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 < num > 20:
        print('Tente novamente.',end='')
    if num > 0 and num <= 20:
        print(f'Você digitou o número: {números[num]}')
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        print('PROGRAMA ENCERRADO.')
        break




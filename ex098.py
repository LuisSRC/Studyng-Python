#Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 30)
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(cont, end=' ')
            sleep(0.4)
            cont += passo
        print('FIM')
    elif inicio > fim:
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.4)
            cont -= passo
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem: ')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)























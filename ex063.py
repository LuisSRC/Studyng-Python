#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
núm = int(input('Quantos termos da Sequencia de Fibonacci você quer ver?: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} → {t2} → ', end='')
while cont <= núm:
    t3 = t1 + t2
    print(f'{t3} →', end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')



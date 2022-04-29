#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo
# , cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
jogos = []
tot = 1
print('-' * 30)
print('{:^30}'.format("JOGANDO NA MEGA SENA"))
print('-' * 30)
quant = int(input('Quantos sorteios você quer que eu faça?: '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    tot += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 3, 'BOA SORTE!! ', '-=' * 3)













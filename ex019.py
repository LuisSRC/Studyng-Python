import math
#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
alunos = []
for c in range(0, 4):
    alunos.append(str(input('Digite o nome do aluno: ')))
print(f'O aluno escolhido foi: {random.choice(alunos)}')




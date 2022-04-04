#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
alunos = []
for c in range(0, 4):
    alunos.append(str(input('Digite o nome do aluno: ')))
random.shuffle(alunos)
print(alunos)

#Exercício Python 026: Faça um programa que leia uma frase pelo teclado
#e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Existem {frase.count("A")} letras "A" na frase.')
print(f'A letra "A" aparece na primeira vez na posição: {frase.find("A")+1}')
print(f'A letra "A" apareceu na ultima vez na posição: {frase.rfind("A")+1}')

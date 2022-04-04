#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
tabuada = int(input('Digite o número para ver a sua tabuada: '))
for c in range(1, 11):
    print(f'{tabuada} x {c} = {tabuada * c}')


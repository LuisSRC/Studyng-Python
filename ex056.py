#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
média = somaidade = idademaisvelho = totmulher20 = 0
nomemaisvelho = ''
for pessoa in range(1, 5):
    print(f'------{pessoa}ªPESSOA------')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade
    média = somaidade / 4
    if pessoa == 1 and sexo == 'M':
        idademaisvelho = idade
        nomemaisvelho = nome
    if idade > idademaisvelho and sexo == 'M':
        idademaisvelho = idade
        nomemaisvelho = nome
    if idade < 20 and sexo == 'F':
        totmulher20 += 1
print(f'A soma da idade das pessoas registradas foi de {somaidade}')
print(f'A média de idade é de {média}')
print(f'A idade do mais velho é de {idademaisvelho} anos de idade e o seu nome é: {nomemaisvelho}')
print(f'{totmulher20} mulheres tem menos de 20 anos.')

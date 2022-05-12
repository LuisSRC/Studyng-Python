#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas
# , guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
pessoas = {}
listapessoas = []
soma = 0
média = 0
while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    pessoas['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoas['Sexo'] not in 'MF':
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    listapessoas.append(pessoas.copy())
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
média = soma / len(listapessoas)
print(f'-A) O grupo tem {len(listapessoas)} pessoas.')
print(f'-B) A média de idade do grupo é de {média} anos de idade.')
print('-C)  As mulheres cadastradas foram: ', end='')
for p in listapessoas:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print('-D) As pessoas com idade acima da média são: ', end='')
for p in listapessoas:
    if p['Idade'] >= média:
        print()
        for k, v in p.items():
            print(f'{k} = {v}')
print(' << ENCERRADO >>')





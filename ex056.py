idademaisvelho = 0
nomevelho = ''
somaidade = 0
mediaidade = 0
cont20mulher = 0
for p in range(1, 5):
    print('------`{}ªPESSOA------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:[M/F]: ')).upper()
    somaidade += idade
    mediaidade = somaidade / 4
    if p == 1 and sexo == 'M':
        nomevelho = nome
        idademaisvelho = idade
    if sexo == 'M' and idade > idademaisvelho:
        idademaisvelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        cont20mulher += 1
print('A média de idade do grupo é de {}anos'.format(mediaidade))
print('O Homem mais velho se chama {} e tem {} anos de idade'.format(nomevelho, idademaisvelho))
print('Existem {} mulheres menores de 20 anos'.format(cont20mulher))






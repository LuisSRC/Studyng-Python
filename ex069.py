cont18 = conthomem = contmulher20 = 0
while True:
    print('------ CADASTRAR PESSOA ------')
    idade = int(input('Idade: '))
    if idade > 18:
        cont18 += 1
    sexo = str(input('Sexo [M/F]')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).strip().upper()[0]
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and idade < 20:
        contmulher20 += 1
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        print('PROGRAMA FINALIZADO')
        break
print(f'{cont18} pessoas tem mais de 18 anos')
print(f'{conthomem} homens foram cadastrados.')
print(f'{contmulher20} mulheres tem menos de 20 anos.')

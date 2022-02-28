sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
if sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados invalidos, por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor, informe seu sexo: ')).strip().upper()[0]
    print('Sexo {} registrado com sucesso'.format(sexo))

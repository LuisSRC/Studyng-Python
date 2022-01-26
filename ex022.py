n = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em letras MAIÚSCULAS é {} '.format(n.upper()))
print('Seu nome em letras minúsculas é {} '.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
divide = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(divide[0], len(divide[0])))









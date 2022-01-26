f = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes na frase'.format(f.count("A")))
print('A primeira letra "A" apareceu na posição {}'.format(f.find('A')))
print('A ultima letra "A" apareceu na posição {}'.format(f.rfind('A')))

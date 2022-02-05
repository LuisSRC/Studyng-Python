num = int(input('Digite um número inteiro qualquer: '))
print('''ESCOLHA A BASE DE CONVERSÃO: '
[  1  ] PARA BINÁRIO
[  2  ] PARA OCTAL
[  3  ] PARA HEXADECIMAL''')
opção = int(input('Digite a opção desejada!: '))
if opção == 1:
    print('{} convertido em BINÁRIO é: {:b}'.format(num, num))
elif opção == 2:
    print('{} convertido em OCTAL é: {:o}'.format(num, num))
elif opção == 3:
    print('{} convertido em HEXADECIMAL é: {:x}'.format(num, num))
else:
    print('Opção inválida! Tente novamente.')








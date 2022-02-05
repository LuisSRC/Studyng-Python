n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {} a média é: {}'.format(n1, n2, media))
if media < 5:
    print('O aluno está REPROVADO!!')
elif media >= 5.0 and media <= 6.9:
    print('O aluno está em RECUPERAÇÃO')
elif media >= 7:
    print('O aluno está APROVADO')



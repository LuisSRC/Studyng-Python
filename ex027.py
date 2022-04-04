#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa
# , mostrando em seguida o primeiro e o último nome separadamente.
nomecompleto = str(input('Digite o nome completo: ')).split()
print(f'O primeiro nome é: {nomecompleto[0]}')
print(f'O ultimo nome é: {nomecompleto[-1]}')

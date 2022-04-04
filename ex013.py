#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário do funcionário: R$'))
novo = salario + (salario * 15 / 100)
print(f'O funcionário que recebia R${salario:.2f} com reajuste de 15% passará a receber: R${novo:.2f}')

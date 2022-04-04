#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o salario do funcionario? R$'))
print(f'Um funcionario com sálario de R${salario:.2f}')
if salario > 1250:
    novo = salario + (salario * 10 / 100)
    print(f'Receberá um aumento de 10% e seu novo salário será de R${novo:.2f}')
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(f'Receberá um aumento de 15% e seu novo salário será de R${novo:.2f}')


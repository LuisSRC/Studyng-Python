salario = float(input('Qual é o salário do funcionario? R$'))
novo = salario + (salario * 15 /100)
print('O novo salario do funcionário que ganhava R${:.2f}, com reajuste de 15% passará a ser R${:.2f}'.format (salario, novo))

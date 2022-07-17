#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, show=False):
    """
    --> Calcula o fatorial de um número.
    :param num: número a ser realizado o calcúlo.
    :param show: (opcional), indica se deve ou não mostrar a conta.
    :return: retorna o resultado da função.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print('-' * 30)
help(fatorial)






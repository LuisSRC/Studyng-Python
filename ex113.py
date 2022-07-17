#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104
# , incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro. Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro. Usuario preferiu não digitar um valor.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = str(input(msg)).replace(',', '.')
            return float(n)
        except (ValueError, TypeError):
            print('\033[31mErro. Digite um número flutuante válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro. Usuario preferiu não digitar um valor.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi: {n1} e o valor real foi: {n2}')






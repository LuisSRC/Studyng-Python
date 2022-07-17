def aumentar(p=0, taxa=0, formato=False):
    resp = p + (p * taxa / 100)
    return resp if formato is False else moeda(resp)


def diminuir(p=0, taxa=0, formato=False):
    resp = n = p - (p * taxa / 100)
    return resp if not formato else moeda(resp)


def dobro(p=0, formato=False):
    resp = p * 2
    return resp if formato is False else moeda(resp)


def metade(p=0, formato=False):
    resp = p / 2
    return resp if formato is False else moeda(resp)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(p=0, aumento=10, reduzir=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR"}'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(p, aumento, True)}')
    print(f'{reduzir}% de redução: \t{diminuir(p, reduzir, True)}')
    print('-' * 30)







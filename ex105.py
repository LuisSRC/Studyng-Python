#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um
# dicionário com as seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)
#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(* nota, sit=False):
    """
    --> Função para analisar notas e situação de varios alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionario com varias informações sobre a situação da turma.
    """
    ficha = dict()
    ficha['total'] = len(nota)
    ficha['maior'] = max(nota)
    ficha['menor'] = min(nota)
    ficha['media'] = sum(nota) / len(nota)
    if sit:
        if ficha['media'] >= 7:
            ficha['situacao'] = 'BOA'
        elif ficha['media'] >= 5:
            ficha['situacao'] = 'RAZOAVEL'
        else:
            ficha['situacao'] = 'RUIM'
    return ficha


resp = notas(5.5, 2.5, 8, 9, 10, sit=True)
print(resp)

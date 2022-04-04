#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1+ r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar um Triangulo.')
    if r1 == r2 == r3:
        print('Triangulo Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Triangulo Escaleno.')
    else:
        print('Triangulo Isósceles.')
else:
    print('Os segmentos NÃO formam um triangulo.')

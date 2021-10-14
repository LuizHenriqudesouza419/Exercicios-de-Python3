#Analisando Triângulos v2.0
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo ')
    if r1 == r2 == r3:
        print('E o triângulo é Equilátero')
    elif r1 != r2 != r3 != r1:
        print('E o triãngulo é Isóceles')
    else:
        print('E o triângulo e Escaleno')

else:
    print('Os segmentos não podem formar um triângulo ')
 
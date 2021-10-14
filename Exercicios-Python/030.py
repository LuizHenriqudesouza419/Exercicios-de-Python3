# Par ou Impar
número = int(input('Me diga um número: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é Par. '.format(número))
else:
    print('O número {} é Impar.'.format(número))
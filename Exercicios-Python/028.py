#jogo de advinhação
from random import randint
computador = randint(0, 5) # faz o computador pensar
print('-+-'*20)
print('Vou pensar em um numero de 1 a 5. Tente advinhar! ')
print('-=-'*20)
jogador = int(input('Qual numero eu pensei ? '))
if jogador == computador:
    print('Vocẽ venceu!!!')
else:
    print('Você perdeu eu pensei no numero {}'.format(computador))
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções: 
[ 0 ] Pedra 
[ 1 ] Papel 
[ 2 ] Tesoura ''')
jogador = int(input('Qual sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('Usuario  jogou {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: # computador jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada Inválida!')
elif computador == 1: # computador jogou Papel
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada Inválida! ')
elif computador == 2: # computador jogou Tesoura
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')

    else:
        print('Jogada Inválida!')


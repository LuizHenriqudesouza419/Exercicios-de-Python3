# Jogo de adivinhaçãp v2.0
from random import randint
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre o e 10.')
print('Será que vocẽ consegue adivinhar qual foi ? ')
acertou = False
palpites = 0
while not acertou:
    palpites += 1
    jogador = int(input('Qual seu palpite? '))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente outra vez')
        elif jogador > computador:
            print('Menos... tente outra vez')
print('Acertou com {} tentativas. Parabéns'.format(palpites))

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpLl':
        tipo = str(input('Par ou Impar ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}.Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Vocẽ perdeu! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Vocẽ venceu!')
            v += 1
        else:
            print('Você perdeu!')
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {v} vezes ')
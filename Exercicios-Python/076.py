listagem = ('lapis', 1.75,
          'Borracha', 2,
          'Caderno', 15.90,
          'Estojo', 25,
          'Trasferidor', 4.20,
          'Compasso', 9.90,
          'Mochila ', 120.30,
          'Canetas', 22.90,
          'Livros', 100)
print('Listagem de preços:')
print('--' * 17)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<25}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

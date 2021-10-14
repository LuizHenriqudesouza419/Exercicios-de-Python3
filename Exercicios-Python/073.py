# Tuplas com Times de Futebol
times = ('Corinthias', 'Palmeiras', 'Santos ', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlétiico', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC vitória', 'Coritiba', 'Avaí', 'P onte Preta',
         'Atlético-GO')
print('--*--' *19)
print(f'Lista de times do Brasileirão: {times}')
print('--*--' * 19)
print(f'Os 5 primeiros times são : {times[0:5]}')
print('--*--' *19)
print(f'Os ultimos 5 times são: {times[-4:]}')
print('--*--' *19)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense") + 1} posição')



# Valores únicos em uma lista 
Números  = []
while True:
    n = int(input(f'digite um valor: '))
    if n not in Números:
        Números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
Números.sort(3)
print(f'Você digitou o3s valores {Números}')


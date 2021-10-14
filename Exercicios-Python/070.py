total = totmil = menor = cont =  0
barato = 0
while True:
    produto = str(input('Nome do Produto '))
    preço = float(input('Preço R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN ':
        resp = str(input('Quer continuar [S/N ]').strip().upper())[0]
    if resp == 'N':
        break
print('{:-^40}'.format('fim do programa '))
print(f'O Total de compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'0 profuto maus barato foi {barato} custa R${menor}')

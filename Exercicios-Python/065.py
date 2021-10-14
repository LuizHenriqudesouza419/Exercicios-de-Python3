resp = 'S'
media = soma = quant = 0
while resp in 'Ss':
    núm = int(input('Didite  um número: ').upper())
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} e a média foi {}'.format(quant, media))
print('O menor valor foi {} e o maior foi {}'.format(menor, maior))


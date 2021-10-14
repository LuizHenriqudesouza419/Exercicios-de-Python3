#custo da viagem
distância = float(input('Qual é a diśtância da sua viagem?  '))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço de sua passagem será de R${:.2f}.'.format(preço))

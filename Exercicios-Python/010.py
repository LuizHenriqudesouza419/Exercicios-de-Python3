#Conversor de Moedas
real = float(input('Quanto dinheiro vocẽ tem na carteira? R$ '))
dolar = real / 5.39
print('Com {:.2f} reais você pode comprar US${:.2f} dolar'.format(real, dolar))

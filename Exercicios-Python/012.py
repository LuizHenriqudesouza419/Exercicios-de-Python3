# Calculando descontos
produto = float(input('Qual o valor do produto ? R$ '))
novo = produto - (produto * 5 / 100)
print('O produto com 5% de desconto ficara : R$ {:.2f} '.format(novo))

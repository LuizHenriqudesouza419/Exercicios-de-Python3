# Reajuste salarial
salário = float(input('Qual seu salário atual ? R$'))
novo = salário + (salário * 15 / 100)
print('Com 5% de aumento seu novo salário é R${:.2f}'.format(novo))

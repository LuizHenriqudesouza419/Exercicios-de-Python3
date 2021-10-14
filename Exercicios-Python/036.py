#Aprovando Empréstimo
casa = float(input('Qual o valor da casa: RS '))
salário = float(input('Qual é seu salário: R$ '))
anos = int(input('Quantas anos de financiamento ? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para  pagar uma casa de R${:.2f} em {} '.format(casa, anos), end='')
print('a prestção será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo Negado ')

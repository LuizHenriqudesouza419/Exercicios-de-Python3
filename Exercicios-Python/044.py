preço = float(input('Qual o valor da sua compra: R$ '))
opção = int(input('''Formas de pagamento 
[ 1 ]  à vista em dinheiro 
[ 2 ]  à vista no cartão 
[ 3 ]  2x no cartão 
[ 4 ]  3x ou mais no cartão
Digite o número que corresponde a forma de pagamento: '''))
if opção == 1:
    desconto = preço - (preço * 10 / 100)
    print('O valor de suas compras é R${:.2f} e com 10%  de desconto em dinheiro ficou R${:.2f} '.format(preço, desconto))
elif opção == 2:
    desconto = preço - (preço * 5 / 100)
    print('O valor de suas compras é R${:.2f} e com 5% de desconto a vista no cartão ficou R${:.2f}'.format(preço, desconto))
elif opção == 3:
    parcela = preço / 2
    print('O valor de suas compras é R${:.2f} e em 2x o valar de cada parcela vai ser R$ {:.2f}'.format(preço, parcela))
elif opção == 4:
    juros = preço + (preço * 20/100)
    parcelas = int(input('Quantas parcelas você deseja fazer o pagamento: '))
    parcial = juros / parcelas
    print('Suas comprar em {}x terá um acréscimo de 20% o total será R${:.2f} eo valor de cada parcela será R${:.2f}'.format(parcelas, juros, parcial))

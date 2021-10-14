velocidade = float(input('Qual é a velocidade atual do carro ? '))
if velocidade > 80:
    print('Multado! Você exedeu o limite permitido que é de 80Km/h.')
    mulra = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${}.'.format(mulra))
print('Bom dia dirija com cuidado!!! ')

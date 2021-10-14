#Aumento salarial
salário = float(input('Qual é o seu salario ? '))
if salário <= 1250.00:
    novo = salário + (salário * 15 / 100)
    print('Seu novo salário com 15% de aumento ficou {}'.format(novo))
else:
    novo = salário + (salário * 10 / 100)
    print('Seu salário com 10% de aumento ficou {}'.format(novo))

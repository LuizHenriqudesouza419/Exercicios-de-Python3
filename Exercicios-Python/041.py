#Classificando Atletas
from datetime import date
atual = date.today().year
nasc= int(input('Em que ano você nasceu? '))
idade = atual - nasc
print('O atleta tem {} anos '.format(idade))
if idade <= 9:
    print('Classificação: MIRIM ')
elif idade <= 14:
    print('Classificação: IFANTIL ')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR ')
elif idade <= 25:
    print('Classificação: MASTER ')
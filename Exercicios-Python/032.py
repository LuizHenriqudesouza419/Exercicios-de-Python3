# Ano bissexto
from datetime import date
print('Coloque 0 para analisar o ano atual')
ano = int(input('Que ano quer analisar?'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))

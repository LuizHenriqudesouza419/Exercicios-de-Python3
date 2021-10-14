#Procurando uma string dentro de outra
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem silva {}'.format('SILVA' in nome.upper()))


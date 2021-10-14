#Analisando Texto
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {} '.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem  ao todo {} letras '.format(len(nome) - nome.count(' ')))
sepera = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(sepera[0], len(sepera[0])))
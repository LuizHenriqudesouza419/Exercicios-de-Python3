# Separando dígitos de um número
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
s = num // 100 % 10
m = num // 100 % 10
print('Analisando o número {}'.format(num))
print('UNIDADE: {}'.format(u))
print('DEZENA: {} '.format(d))
print('CENTENA:{} '.format(s))
print('MILHAR: {} '.format(m))

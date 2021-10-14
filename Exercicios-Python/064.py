num = cont = soma = 0
num = int(input('Digite um número [OU 999 PARA CANCELAR]'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [OU 999 PARA CANCELAR]'))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))

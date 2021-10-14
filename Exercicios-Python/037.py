#Conversor de bases
num = int(input('Digite um número inteiro: '))
print('''Escolha uma da bases númericas para a conversão 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] convervter para HEXADECIMAL''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print('O número {} convertido para Binário é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida.Tente novamente')

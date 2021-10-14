# Número por Extenso
cont = ('zero','um','dois','três', 'quatro ',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete','dezoito',
        'dezenove', 'vinte ')
while True:
        número = int(input(' Digite um número entre 0 a 20: '))
        if 0 <= número <= 20:
                break
        print('Tente novamente', end='')
print(f'Você digitiu o número {cont[número]}')


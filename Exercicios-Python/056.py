somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('---- {}ª PESSOA ---- '.format(p))
    Nome = str(input('Nome: ')).strip()
    Idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F] ')).strip()
    somaidade += Idade
    if p == 1 and Sexo in 'Mm':
        maioridadehomem = Idade
        nomevelho = Nome
    if Sexo in 'Mm' and Idade > maioridadehomem:
        maioridadehomem = Idade
        nomevelho = Nome
    if Sexo in 'Ff' and Idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade de grupo ŕ do {} anos '.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos '.format(totmulher20))

# Media do aluno
n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
média = (n1 + n2 + n3) / 3
if média <= 5:
    print('Sua média é {} e você foi reprovado. '.format(média))
elif 7 > média >= 5:
    print('Sua média é {} e você esta de recuperação. '.format(média))
elif média >= 7:
    print('Sua média é {} parabens você passou de ano. '.format(média))

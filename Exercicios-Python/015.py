# Alugel de carro
dias = int(input('Quantos dias você ficou com o carro ? '))
km = float(input('Quantos km vocẽ andou ? '))
pagar = (60 * dias) + (km * 0.46)
print('Você ficou com o carro durante {} e rodou {}km e tera que pagar {:.f}'.format(dias, km, pagar))

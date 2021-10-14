# Pintando parede
al = float(input('Didite a altura da sua parede; '))
lar = float(input('Digite a largura da sua parede; '))
area = al * lar
tinta = area / 2
print('Sua parede tem as dimençães de {}x{} sua area é {:.2f} metros cubicos e você vai precisar de {:.2f}l de tinta'.format(al, lar, area, tinta))
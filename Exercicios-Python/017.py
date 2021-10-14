# Catetos da hipotenusa
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#hi = (ca ** 2 + co **2) ** 1/2'''
hi = hypot(co, ca)
print(hi)

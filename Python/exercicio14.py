# Hipotenusa 2

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = math.hypot(co, ca)

print('A hipotenusa valerá {:.2f}!'.format(hi))


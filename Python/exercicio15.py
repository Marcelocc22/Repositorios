# Seno, Cosseno e Tângente.

import math

ang = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(ang))
print('O ângulo {} tem o Seno de {:.2f}'.format(ang, seno))

cos = math.cos(math.radians(ang))
print('O ângulo {} tem o Cosseno de {:.2f}'.format(ang, cos))

tan = math.tan(math.radians(ang))
print('O ângulo {} tem a Tângente de {:.2f}'.format(ang, tan))




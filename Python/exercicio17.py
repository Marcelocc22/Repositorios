# Embaralhando

import random

name1 = str(input('Primeiro nome: '))
name2 = str(input('Segundo nome: '))
name3 = str(input('Terceiro nome: '))
name4 = str(input('Quarto nome: '))

list = [name1, name2, name3, name4]

random.shuffle(list)

print('A ordem será ')
print(list)

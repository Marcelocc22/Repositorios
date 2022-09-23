# Aluguel de Carros

dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos Km foram rodados? '))
preco = (dias * 60) + (km * 0.15)
print('O total a se pagar é R${:.2f}'.format(preco))


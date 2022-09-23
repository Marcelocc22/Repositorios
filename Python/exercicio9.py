# Reajuste Salarial


salario = float(input('Qual é o salário do funcionario? R$'))
reajuste = salario + (salario * 15 / 100) 
print('O funcionário que ganhava R${:.2f}, com reajuste de 15% receberá: R${:.2f}').format(salario, reajuste)



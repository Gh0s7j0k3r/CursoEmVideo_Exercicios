'''Escreva um programa que pergunte o salario de um funcionario e 
calcule o valor do seu aumento.
Para salarios superiores a R$1250.00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento e de 15%.'''

salario=float(input('Informe o salario: R$'))
if salario > 1250:
    print('Para um aumento de 10%, o salario vai passar de R${:.2f} para R${:.2f}.'.format(salario,salario*1.10))
else:
    print('Para um aumento de 15%, o salario vai passar de R${:.2f} para R${:.2f}.'.format(salario,salario *1.15))
print('Obrigado!')
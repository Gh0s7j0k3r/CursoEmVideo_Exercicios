'''faco um algoritmo que leia o salario de um funcionario e 
mostre seu novo salario, com 15% de aumento.'''

salario=float(input('Informe o seu salario: R$'))
print('Com um aumento de 15% para o salario R${:.2f}, o mesmo passa a ser R${:.2f}'.format(salario,salario*1.15))

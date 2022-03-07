'''Escreva um programa para aprovar o emprestimo bancario para a compra
de uma casa. O programa vai perguntar o valor da casa, o salario do 
comprador e em quantos anos ele vai pagar.
Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 
30% do salario ou entao o emprestimo sera negado.'''

casa=float(input('Informe o valor da casa: R$'))
salario=float(input('Informe o seu salario: R$'))
periodo=int(input('Informe em quantos anos deseja quitar: '))
tempo=periodo*12
parcela=casa/tempo
comprometimento=salario*0.30
if comprometimento < parcela:
    print('Para o tempo selecionado nao vai ser possivel realizar o emprestimo devido ao maximo permitido de comprometimento de sua renda.')
else:
    print('Para o periodo de {} meses, o valor da parcela vai ser de R${:.2f}.'.format(tempo,parcela))

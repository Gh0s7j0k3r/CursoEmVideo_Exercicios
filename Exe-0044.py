'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preco normal e condicao de pagamento:
A vista dinheiro/cheque: 10% de desconto
A vista no cartao: 5% de desconto
em ate 2x no cartao: preco normal
3x ou mais no cartao: 20% de juros'''

valor=float(input('Informe o valor do produto: R$'))
print('Qual a forma de pagamento?\n\033[1;31m1-\033[mA vista dinheiro/cheque\n\033[1;31m2-\033[mA vista no cartao\n\033[1;31m3-\033[mEm ate 2x no cartao de credito\n\033[1;31m4-\033[m3x a 12x no cartao de credito')
pag=int(input('Informe qual sua opcao de pagamento conforme opcoes acima: '))
if pag == 1:
    print('Para pagamento a vista dinheiro/cheque voce tem 10% de desconto, o valor passa de R${:.2f} e voce paga apenas R${:.2f}.'.format(valor,valor*0.90))
elif pag == 2:
    print('Para pagamento a vista no cartao voce tem 5% de desconto, o valor passa de R${:.2f} e voce paga apenas R${:.2f}.'.format(valor,valor*0.95))
elif pag == 3:
    print('Para pagamento em 2x no cartao o valor a ser pago e R${:.2f} e o valor de cada parcela vai ser R${:.2f} sem juros.'.format(valor,valor/2))
elif pag == 4:
    parcela=int(input('Informe a quantidade de parcelas: '))
    print('Para pagamento de 3x ate 12x e cobrado 20% de juros, dessa forma um produto que custava R${:.2f}, voce paga R${:.2f}, e cada parcela fica R${:.2f} com juros em {}x.'.format(valor,valor*1.20, (valor*1.20)/parcela,parcela))
else:
    print('Opcao invalida, por favor, escolha de 1 a 4 a melhor forma que lhe atende!')

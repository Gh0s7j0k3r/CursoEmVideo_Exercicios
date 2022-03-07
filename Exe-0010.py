'''crie um programa que leia quanto dinheiro uma pessoa 
tem na carteira e mostre quantos dolares ela pode comprar'''
dinheiro=float(input('Informe a quantidade de dinheiro para compra de dolar: R$'))
cad=4.43
dolar=5.72
dolartur=5.97
print('Com R${:.2f} e possivel comprar CAD${:.2f} em dolar canadense.\nCom R${:.2f} e possivel comprar US${:.2f} em dolar comercial.\nCom R${:.2f} e possivel comprar US${:.2f} em dolar turismo'.format(dinheiro,dinheiro/cad,dinheiro,dinheiro/dolar,dinheiro,dinheiro/dolartur))

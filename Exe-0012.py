'''faca um algoritmo que leia o preco de um produto e 
mostre seu novo preco, com 5% de desconto.'''

prod=float(input('Informe o valor do produto: R$'))
print('O valor do produto e: R${:.2f} e com desconto de 5% passa a ser R${:.2f}'.format(prod,prod*0.95))

'''Crie um programa que leia o nome e o preco de varios produtos. O 
programa devera perguntar se o usuario vai continuar. No final, mostre:
A-Qual e o total gasto na compra.
B-Quantos produtos custam mais de R$1000.
C-Qual e o nome do produto mais barato.'''

total = cont = barato = 0
while True:
    produto=str(input('Nome do produto: '))
    preco=float(input('Preco: R$'))
    total += preco
    if preco > 1000:
        cont += 1
    if total == preco or preco < barato:
        barato = preco
        prodbarato = produto
    #else:
        #if preco < barato:
            #barato = preco
            #prodbarato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prodbarato} que custava R${barato:.2f}')
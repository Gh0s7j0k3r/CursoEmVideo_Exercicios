'''Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor a ser sacado(numero inteiro) e o programa vai informar
quantas cedulas de cada valor serao entregues. OBS:Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1.'''

valor=int(input('Que valor voce quer sacar? R$'))
total = valor
cont50 = cont20 = cont10 = cont = 0
while True:
    while total >= 50:
        total -= 50
        cont50 += 1
    print(f'Total de {cont50} cedulas de R$50')
    while total >= 20:
        total -= 20
        cont20 += 1
    print(f'Total de {cont20} cedulas de R$20')
    while total >= 10:
        total -= 10
        cont10 += 1
    print(f'Total de {cont10} cedulas de R$10')
    while total >= 1:
        total -= 1
        cont += 1
    print(f'Total de {cont} cedulas de R$1')
    if total == 0:
        break
print('Volte sempre!!!')

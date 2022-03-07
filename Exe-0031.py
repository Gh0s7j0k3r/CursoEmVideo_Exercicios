'''Desenvolva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preco da passagem, cobrando R$0.50 por Km para viagens
de ate 200Km e R$0.45 para viagens mais longas.'''

km=float(input('Informe a distancia em KM para a viagem: '))
if km <= 200:
    print('O valor da passagem vai ser R${:.2f}.'.format(km*0.50))
else:
    print('O valor da passagem vai ser R${:.2f}.'.format(km*0.45))
print('Boa viagem!')

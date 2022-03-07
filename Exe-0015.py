'''Escreva um programa que pergunte a quantidade de Km percorridos por
um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preco a pagar, sabendo que o carro custa R$60 por dia 
e R$0.15 por Km rodado.'''

km=float(input('Informe a quantidade de Km`s percorridos: '))
diaria=int(input('Informe a quantidade de dias com o veiculo: '))
dia=60*diaria
kmr=0.15*km
print('O valor a pagar devido aos {}Km utilizados e {} diarias utilizadas e R${:.2f}'.format(km,diaria,kmr+dia))

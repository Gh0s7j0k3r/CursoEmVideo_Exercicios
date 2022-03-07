'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80KM/h. mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada KM acima do limite.'''

velocidade = int(input('Informe a velocidade do veiculo: '))
if velocidade > 80:
    print('Sua velocidade esta superior em {}Km\h ao permitido, desta forma, seu veiculo foi multado em R${:.2f}'.format(velocidade-80,(velocidade-80)*7))
else:
    print('Voce esta dentro da velocidade permitida!')
print('Boa viagem!')

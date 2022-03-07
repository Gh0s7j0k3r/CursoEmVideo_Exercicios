'''Faca um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador perder, mostrando o total de 
vitorias consecutivas que ele conquistou no final do jogo.'''
from random import randint
print('Vamos jogar Par ou Impar?')
cont = 0
while True:
    comp=randint(0,10)
    escolha = " "
    while escolha not in 'PpIi':
        escolha=str(input('Par ou Impar? [P/I]')).upper().strip()[0]
    hum=int(input('Digite um valor: '))
    soma = (comp + hum)
    if soma % 2 != 1:
        term = str('Deu PAR')
        resultado = 'P'
    else:
        term = str('Deu IMPAR')
        resultado = 'I'
    print('-'*30)
    print(f'Voce jogou {hum} e o computador {comp}. Total de {soma}, {term}.')
    print('-'*30)
    if resultado == escolha:
        print('Voce VENCEU!\nVamos jogar novamente...')
        print('-='*15)
    else:
        print('Voce PERDEU!')
        print('-='*15)
        break
    cont += 1
print(f'GAME OVER! Voce venceu {cont} vezes.')

'''Escreva um programa que faca o computador "pensar" em um numero inteiro
entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero 
escolhido pelo computador.
O programa devera escrever na tela se o usuario venceu ou perdeu.'''

from random import randint
num=int(input('Informe um numero de 0 a 5 que o computador esta "pensando": '))
numpc=randint(0,5)
if num == numpc:
    print('Parabens, voce ganhou! \nVoce e o computador escolheram o mesmo numero {}.'.format(numpc))
else:
    print('Que pena, voce perdeu! \nO numero escolhido pelo computador foi {}. \nNao desista, tente novamente!'.format(numpc))
print('Obrigado por participar deste jogo!')
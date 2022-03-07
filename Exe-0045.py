'''Crie um programa que faca o computador jogar jokenpo com voce.'''

from random import choice
from time import sleep
print('''Suas opcoes:
[0] Pedra
[1] Papel
[2] Tesoura''')
num=int(input('Qual e sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
lista=choice(['Pedra', 'Papel', 'Tesoura'])
if num == 0:
    escolha='Pedra'
    if lista == 'Pedra':
        print('Voce escolheu {}, o computador escolheu {}, deu empate.'.format(escolha,lista))
    elif lista == 'Papel':
        print('Voce escolheu {}, o computador escolheu {}, voce perdeu!'.format(escolha,lista))
    else:
        print('Voce escolheu {}, o computador escolheu {}, voce ganhou!'.format(escolha,lista))
elif num == 1:
    escolha='Papel'
    if lista == 'Papel':
        print('Voce escolheu {}, o computador escolheu {}, deu empate.'.format(escolha,lista))
    elif lista == 'Tesoura':
        print('Voce escolheu {}, o computador escolheu {}, voce perdeu!'.format(escolha,lista))
    else:
        print('Voce escolheu {}, o computador escolheu {}, voce ganhou!'.format(escolha, lista))
elif num == 2:
    escolha='Tesoura'
    if lista == 'Tesoura':
        print('Voce escolheu {}, o computador escolheu {}, deu empate.'.format(escolha, lista))
    elif lista == 'Pedra':
        print('Voce escolheu {}, o computador escolheu {}, voce perdeu!'.format(escolha,lista))
    else:
        print('Voce escolheu {}, o computador escolheu {}, voce ganhou!'.format(escolha,lista))
else:
    print('Numero invalido! Tente novamente!')

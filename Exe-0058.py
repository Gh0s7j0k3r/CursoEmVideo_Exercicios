'''Melhore o jogo do Desafio028 onde o computador vai "pensar" em um 
numero entre 0 e 10. So que agora o jogador vai tentar adivinhar ate
acertar, mostrando no final quantos palpites foram necessarios para
vencer.'''

from random import randint
print('''Sou seu computador..
Acabei de pensar em um numero entre 0 e 10.
Sera que voce consegue adivinhar qual foi?''')
num=int(input('Qual e seu palpite? '))
cont = 1
numpc=randint(0,10)
while num != numpc:
    cont += 1
    if num > numpc:
        print('Menos... Tente mais uma vez.')
        num=int(input('Qual e seu palpite? '))
    elif num < numpc:
        print('Mais... Tente mais uma vez.')
        num=int(input('Qual e seu palpite? '))
print('Acertou com {} tentativas. Parabens!'.format(cont))

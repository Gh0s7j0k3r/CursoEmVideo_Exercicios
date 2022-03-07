'''Faca um porograma que mostre na tela uma contagem regressiva para 
o estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 
1 segundo entre eles.'''

from time import sleep
print('Contagem regressiva: ')
for c in range(11,0,-1):
    print(c-1)
    sleep(1)
print('Fim')
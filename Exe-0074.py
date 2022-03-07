'''Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla.'''

import random
sorteio = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
print(f'Os numeros sorteados foram: ',end='')
for n in sorteio:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {sorted(sorteio)[-1]}')
print(f'O menor valor sorteado foi {sorted(sorteio)[0]}')

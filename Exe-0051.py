'''Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
No final, mostre os 10 primeiros termos dessa progressao.'''

primeiro=int(input('Informe o primeiro termo: '))
razao=int(input('Razao: '))
for s in range (1,11):
    print(primeiro, end='-')
    primeiro=primeiro+razao
print('Acabou')

'''primeir=int(input('Primeiro termo: ')) 
razao = int(input('Razao: '))
decimo=primeiro+(10-1)*razao
for c in range (primeiro, decimo+ razao, razao):
    print('{} '.format(c), end='-')
print('Acabou')'''
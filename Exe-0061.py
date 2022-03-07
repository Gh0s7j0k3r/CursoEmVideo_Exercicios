'''Refaca o desafio051, lendo o primeiro termo e a razao de uma PA, mostrando
os 10 primeiros termos da progressao usando a estrutura while.'''

primeiro=int(input('Primeiro termo: '))
razao=int(input('Razao: '))
decimo=primeiro+(10-1)*razao
while primeiro <= decimo:
    print(primeiro,end=' -> ')
    primeiro += razao
print('Fim')

'''print('Gerador de PA')
print('-=' *10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont =1 
while cont <= 10:
    print('{} -> '.format(termo),end='')
    termo += razao
    cont += 1
print('FIM')'''
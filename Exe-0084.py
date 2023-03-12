'''Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
A-Quantas pessoas foram cadastradas.
B-Uma listagem com as pessoas mais pesadas.
C-Uma listagem com as pessoas mais leves.'''

galera = list ()
pessoas = []
cont = leve = pesada = total = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    galera.append(pessoas[:])
    pessoas.clear()
    cont += 1
    resp = str(input('Quer incluir outra pessoa? [S/N] '))
    if resp in 'nN':
        break
for p in range(0,cont):
    total = total + galera[p][1]
media = total / cont
for g in range(0, cont):
    if galera[g][1] <= media:
        leve += 1
        print(f'{galera[g][0]} está abaixo da média de peso deste grupo.')
    else:
        pesada += 1
        print(f'{galera[g][0]} está acima da média de peso deste grupo.')
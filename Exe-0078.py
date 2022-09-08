'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista=list()
maior = menor = 0

for c in range(0,5):
    lista.append(int(input(f'Digite um valor par a posição {c}: ')))
    if c == 0:
        maior=lista[c]
        menor=lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor=lista[c]
print(f'Você digitou os valor {lista}')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print(f'\nO maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')

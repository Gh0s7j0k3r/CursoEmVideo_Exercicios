'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista=list()
cont=0
for c in range(0,5):
    num=int(input('Digite um valor: '))
    lista.append(num)
maior=lista[0]
menor=lista[0]
while cont < 5:
    if lista[cont] >= maior:
        maior = lista[cont]
        cont +=1
print(lista)
print(maior)
print(menor)
print(f'O menor valor apareceu na {lista.index(menor)+1}ª posição.')
print(f'O maior valor apareceu na {lista.index(maior)+1}ª posição.')

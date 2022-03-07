'''Faca um programa que leia o peso de cinco pessoas. No final, mostre 
qual foi o maior e o menor peso lidos.'''

maior=0
menor=0
for c in range (0,5):
    peso=float(input('Informe o peso: '))
    if c == 0:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor=peso
print('O menor peso lido foi: {:.1f}Kg'.format(maior))
print('O menor peso lido foi: {:.1f}Kg'.format(menor))

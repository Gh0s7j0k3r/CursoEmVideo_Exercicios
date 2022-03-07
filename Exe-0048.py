'''Faca um programa que calcule a soma entre todos os numeros impares que
sao multiplos de tres e que se encontram no intervalo de 1 ate 500.'''

soma = 0
cont = 0
for num in range (1,501, 2):
    if num % 3 == 0:
        cont = cont + 1
        soma += num
print('A soma de todos os {} valores solicitados e {}.'.format(cont,soma))

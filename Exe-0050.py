'''Desenvolva um programa que leia seis numero inteiros e mostre a soma 
apenas daqueles que forem pares. Se o valor digitado for impar, 
desconsidere-o.'''

soma = 0
cont = 0
soma1 = 0
cont1 = 0

for c in range(0,6):
    num=int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
    else:
        soma1 = soma + num
        cont1 = cont1 +1
print('A soma de todos os {} valores pares informados e {}.'.format(cont,soma))
print('A soma de todos os {} valores impares informados e {}.'.format(cont1,soma1))
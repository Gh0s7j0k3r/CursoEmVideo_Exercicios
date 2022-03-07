'''Crie um programa que leia um numero inteiro e mostre na 
tela se ele e par ou impar'''

num=int(input('Informe um numero: '))
impar = num % 2
if impar == 1 :
    print('O numero {} e impar.'.format(num))
else:
    print('O numero {} e par.'.format(num))

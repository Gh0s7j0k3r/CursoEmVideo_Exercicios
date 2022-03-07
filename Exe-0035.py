'''Desenvolva um programa que leia o comprimento de tres retas e diga 
ao usuario se elas podem ou nao formar um triangulo.'''

n1=float(input('Informe o comprimento da primeira reta: '))
n2=float(input('Informe o comprimento da segunda reta: '))
n3=float(input('Informe o comprimento da terceira reta: '))
if n1+n2>n3 and n2+n3>n1 and n3+n1>n2:
    print('E possivel formar um triangulo.')
else:
    print('Nao e possivel formar um triangulo.')
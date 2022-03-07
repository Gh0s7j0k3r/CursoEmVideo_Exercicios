'''Faca um programa que leia o comprimento do cateto oposto e 
do cateto adjacente de um triangulo retangulo, 
calcule e mostre o comprimento da hipotenusa.'''

from math import hypot

CatOp=float(input('Comprimento do cateto oposto: '))
CatAd=float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(CatOp,CatAd)))

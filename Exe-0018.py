'''Faca um programa que leia um angulo qualquer e mostre na 
tela o valor do seno, cosseno e tangente desse angulo.'''

from math import sin,cos,tan,radians

angulo=float(input('Informe um angulo: '))
print('Para o angulo {}, o seno e {:.2f}, o cosseno e {:.2f} e a tangente e {:.2f}.'.format(angulo,sin(radians(angulo)),cos(radians(angulo)),tan(radians(angulo))))

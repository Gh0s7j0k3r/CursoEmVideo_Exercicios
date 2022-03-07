'''Faca um programa que leia um numero qualquer e mostre o seu fatorial.
EX:
5!=5x4x3x2x1=120'''

mult=1
num = int(input('Digite um numero: '))
print('{}!='.format(num),end='')
while num >= 2:
    print('{}x'.format(num),end='')
    mult *= num
    num -= 1
print('1={}'.format(mult))

'''for c in range (1,num+1):
    print('{}x'.format(num),end='')
    mult *= num
    num -= 1
print('1={}'.format(mult))'''
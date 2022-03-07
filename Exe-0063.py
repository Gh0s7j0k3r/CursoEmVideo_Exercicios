'''Escreva um programa que leia um numero n inteiro qualquer e mostre na
tela os n primeiros elementos de uma sequencia de fibonacci.
EX:
0-1-1-2-3-5-8'''

print('Sequencia Fibonacci')
print('-='*15)
n=int(input('Quantos numeros? '))
cont=3
soma=1
var=soma
t1 = 0
t2 = 1
print('{} - {}'.format(t1,t2), end="")
while cont <= n:
    cont += 1
    t3 = t1+t2
    print(' - {}'.format(t3),end='' )
    t1 = t2
    t2 = t3
print(' - FIM')

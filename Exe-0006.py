'''Crie um algoritimo que leia um numero e mostre o seu
 dobro, triplo e raiz quadrada'''

num1=int(input('Informe um valor inteiro: '))
print('Para o numero {}, o dobro e {}, o triplo e {} e a raiz quadrada e {:.2f}.'.format(num1,num1*2,num1*3,num1**(1/2)))
'''pow(num1,(1/2)) - Outra forma de fazer a potencia.'''
'''Refaca o desafio 35 dos triangulos, acrescentando o recuso de mostrar 
que tipo de triangulo sera formado:
Equilatero: todos os lados iguais
Isosceles: dois lados iguais
Escaleno: todos os lados diferentes'''

lado1=float(input('Informe o comprimento da primeira reta: '))
lado2=float(input('Informe o comprimento da segunda reta: '))
lado3=float(input('Informe o comprimento da terceira reta: '))
if lado1+lado2>lado3 and lado2+lado3>lado1 and lado1+lado3>lado2:
    print('E possivel formar um triangulo.')
    if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print('Trata-se de um triangulo Isosceles.')
    elif lado1 == lado2 == lado3:
        print('Trata-se de um triangulo Equilatero.')
    else:
        print('Trata-se de um triangulo Escaleno.')
else:
    print('Nao e possivel formar um triangulo. ')
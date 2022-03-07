'''Escreva um programa que leia dois numero inteiros e compare-os 
mostrando na tela uma mensagem: 
O primeiro valor e maior
O segundo valor e maior
Nao existe valor maior, os dois sao iguais'''

num1=int(input('Primeiro numero: '))
num2=int(input('Segundo numero: '))
if num1 > num2:
    print('O primeiro numero informado e maior que o segundo numero.')
elif num2 > num1:
    print('O segundo numero informado e maior que o primeiro.')
else:
    print('O primeiro e segundo numero sao iguais.')
print('Obrigado!')
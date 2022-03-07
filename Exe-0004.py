'''Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele.'''
var1=input('Digite algo: ')
print('O tipo primitivo deste valor e ', type(var1))
print('Pode ser um alfanumerico? {}'.format(var1.isalnum()))
print('Pode ser alfabetico?', var1.isalpha())
print(var1.isascii())
print(var1.isdecimal())
print(var1.isdigit())

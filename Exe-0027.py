'''Faca um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o ultimo nome separadamente.

Ex: Ana maria de souza
Primeiro = Ana
Ultimo = Souza'''

nome=str(input('Informe o nome completo: ')).strip().title().split()
print('Primeiro nome: {} \Ultimo nome: {}'.format(nome[0],nome[-1]))

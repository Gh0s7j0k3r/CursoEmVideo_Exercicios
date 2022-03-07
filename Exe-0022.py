'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas
O nome com todos minusculas
Quantas letras ao todo (sem considerar espacos)
Quantas letras tem o primeiro nome'''

nome=str(input('Informe seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
dividido=nome.split()
print(len(''.join(dividido)))
print(len(dividido[0]))
#print(len(nome) - nome.count(' ')) - Quantidade de letras sem os espacos
#print(nome.find(' ')) - Quantidade de letras tem o primeiro nome.

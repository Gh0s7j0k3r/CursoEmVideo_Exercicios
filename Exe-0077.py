'''Crie um programa que tenha uma tupla com varias palavras 
(nao usar acentos). Depois disso, voce deve mostrar, para cada palavra,
 quais sao as suas vogais.'''

palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'ESTUDAR'
for p in palavras:
    print(f'\nNa palavra {p} temos ',end="")
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=" ")